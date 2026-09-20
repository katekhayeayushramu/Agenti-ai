# app.py
import inspect
import os
import re
import gradio as gr

from schemes import SCHEMES, CATEGORIES


def normalize(text):
    return re.sub(r"[^a-z0-9\s₹]", " ", (text or "").lower()).strip()


def scheme_text(s):
    return " ".join([
        s["name"], s["short_name"], s["category"], s["purpose"],
        s["benefits"], s["eligibility"], " ".join(s["keywords"])
    ])


def search_schemes(query, top_k=3):
    q = normalize(query)
    if not q:
        return []

    q_words = set(q.split())
    scored = []

    for s in SCHEMES:
        searchable = normalize(scheme_text(s))
        score = 0

        # Exact keyword matches get more weight.
        for kw in s["keywords"]:
            if normalize(kw) in q:
                score += 8

        # Name/category/purpose word overlap.
        for word in q_words:
            if len(word) >= 3 and word in searchable:
                score += 1

        if score > 0:
            scored.append((score, s))

    scored.sort(key=lambda x: x[0], reverse=True)
    return [s for _, s in scored[:top_k]]


def format_scheme(s):
    docs = "\n".join(f"- {x}" for x in s["documents"])
    return f"""### 🌾 {s['name']} ({s['short_name']})

**Category:** {s['category']}

**Purpose:**  
{s['purpose']}

**Benefits:**  
{s['benefits']}

**Eligibility:**  
{s['eligibility']}

**Documents commonly required:**  
{docs}

**How to apply:**  
{s['application']}

**Official source:** {s['official_url']}
"""


def retrieval_answer(question):
    matches = search_schemes(question)

    if not matches:
        return (
            "I could not confidently match your question to the schemes in my "
            "current knowledge base.\n\n"
            "Please mention the scheme name, crop, state/district, or what you "
            "need help with (income support, crop insurance, loan, irrigation, "
            "soil testing, marketing, or infrastructure).\n\n"
            "For current eligibility and application rules, always verify the "
            "official government portal."
        )

    answer = "I found the following relevant scheme information:\n\n"
    answer += "\n\n".join(format_scheme(s) for s in matches)

    if len(matches) > 1:
        answer += (
            "\n> **Note:** More than one scheme matched your question. "
            "Eligibility and availability can depend on your state, crop, "
            "season and other conditions."
        )
    return answer


def build_context(matches):
    parts = []
    for s in matches:
        parts.append(
            f"""SCHEME: {s['name']} ({s['short_name']})
CATEGORY: {s['category']}
PURPOSE: {s['purpose']}
BENEFITS: {s['benefits']}
ELIGIBILITY: {s['eligibility']}
DOCUMENTS: {', '.join(s['documents'])}
APPLICATION: {s['application']}
OFFICIAL SOURCE: {s['official_url']}"""
        )
    return "\n\n".join(parts)


def groq_answer(question, history):
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        return None

    try:
        from groq import Groq
        client = Groq(api_key=api_key)

        matches = search_schemes(question, top_k=4)
        context = build_context(matches)

        system = f"""You are Agricultural Scheme Information Agent for India.

Answer only from the supplied knowledge base when discussing a scheme.
Do not invent benefits, eligibility, deadlines, subsidies, application rules,
or documents.

If the knowledge base is insufficient, clearly say that current official
verification is needed.

Important:
- Do not promise that a farmer is eligible.
- Ask for state/district, crop, season, land/cultivation status or other
  missing details when they are necessary.
- Keep the answer simple and farmer-friendly.
- You can answer in English or simple Hindi/Hinglish based on the user's
  language.
- Always encourage verification on the official government source for
  current rules.

KNOWLEDGE BASE:
{context if context else "No scheme matched directly."}
"""

        messages = [{"role": "system", "content": system}]

        # Keep recent conversation only.
        for item in history[-8:]:
            if isinstance(item, dict) and item.get("role") in ("user", "assistant"):
                content = item.get("content")
                if isinstance(content, str):
                    messages.append({
                        "role": item["role"],
                        "content": content
                    })

        messages.append({"role": "user", "content": question})

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=0.2,
        )
        return response.choices[0].message.content

    except Exception as e:
        return (
            "The AI service could not be reached right now. "
            "I can still answer using the local scheme knowledge base.\n\n"
            f"{retrieval_answer(question)}\n\n"
            f"Technical note: {type(e).__name__}"
        )


def answer_question(message, history):
    if not message or not message.strip():
        return history or []

    text = message.strip()
    ai = groq_answer(text, history or [])
    reply = ai if ai else retrieval_answer(text)

    new_history = (history or []) + [
        {"role": "user", "content": text},
        {"role": "assistant", "content": reply},
    ]
    return new_history


def category_search(category):
    if not category or category == "Select a category":
        return "Select a category to see the schemes."

    matches = [s for s in SCHEMES if s["category"] == category]
    if not matches:
        return "No schemes found in this category."

    return "\n\n".join(format_scheme(s) for s in matches)


def clear_chat():
    return [], ""


with gr.Blocks(title="Agricultural Government Scheme Information Agent") as demo:
    gr.Markdown(
        """
# 🌾 Agricultural Government Scheme Information Agent

**Find government agricultural schemes, understand their purpose and benefits,
and learn where to verify eligibility and application information.**

> This is an educational information assistant. It does **not** determine
> final eligibility or submit applications.
"""
    )

    with gr.Row():
        with gr.Column(scale=2):
            chatbot_kwargs = {"label": "🤖 Scheme Assistant", "height": 520}
            if "type" in inspect.signature(gr.Chatbot.__init__).parameters:
                chatbot_kwargs["type"] = "messages"
            chatbot = gr.Chatbot(**chatbot_kwargs)

            question = gr.Textbox(
                label="Ask your question",
                placeholder=(
                    "Example: Which scheme can help with crop insurance?"
                ),
                lines=2
            )

            with gr.Row():
                ask = gr.Button("🔎 Ask Agent", variant="primary")
                clear = gr.Button("🗑️ Clear")

        with gr.Column(scale=1):
            gr.Markdown("### 📚 Browse by category")
            category = gr.Dropdown(
                choices=["Select a category"] + CATEGORIES,
                value="Select a category",
                label="Category"
            )
            category_output = gr.Markdown(
                "Choose a category to view the available schemes."
            )

            gr.Markdown(
                """
### 💡 Try these questions

- Which scheme gives income support to farmers?
- I need crop insurance. Which scheme should I check?
- What is Kisan Credit Card?
- I want to build agricultural infrastructure.
- How can I get information about soil health?
- Where can farmers check agricultural market information?
- I need irrigation support. What should I check?
"""
            )

    ask.click(
        answer_question,
        inputs=[question, chatbot],
        outputs=chatbot
    ).then(
        lambda: "",
        outputs=question
    )

    question.submit(
        answer_question,
        inputs=[question, chatbot],
        outputs=chatbot
    ).then(
        lambda: "",
        outputs=question
    )

    clear.click(
        clear_chat,
        outputs=[chatbot, question]
    )

    category.change(
        category_search,
        inputs=category,
        outputs=category_output
    )

    gr.Markdown(
        """
---
### ⚠️ Important
Government schemes can change. State/district notifications, crop, season,
documents and eligibility conditions may affect the answer. Always verify
current details on the official government portal before applying.
"""
    )


if __name__ == "__main__":
    demo.launch()
