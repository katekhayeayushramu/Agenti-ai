# 🌾 Agricultural Government Scheme Information Agent

A simple AI + Gradio project that helps users find information about
agricultural government schemes in India.

## Features

- Gradio web interface
- Chatbot-style question answering
- Local scheme knowledge base
- Keyword-based scheme retrieval
- Optional Groq + Llama AI response generation
- Category-based scheme browsing
- Official-source links
- English and simple Hindi/Hinglish questions
- Works without a Groq API key using the local knowledge base

## Project structure

```text
agricultural_scheme_agent/
│
├── app.py
├── schemes.py
├── requirements.txt
└── README.md
```

## Step 1: Open terminal

In VS Code, open the project folder and run:

```bash
python -m venv venv
```

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, you can instead run:

```powershell
venv\Scripts\activate.bat
```

## Step 2: Install packages

```bash
pip install -r requirements.txt
```

## Step 3: Optional Groq API key

The project can run without Groq. Without a key it uses local retrieval.

For AI-generated answers, set the environment variable.

PowerShell:

```powershell
$env:GROQ_API_KEY="YOUR_GROQ_API_KEY"
```

Command Prompt:

```cmd
set GROQ_API_KEY=YOUR_GROQ_API_KEY
```

Do not put your real API key directly inside `app.py` or upload it to GitHub.

## Step 4: Run

```bash
python app.py
```

Open the local Gradio URL shown in the terminal, usually something like:

```text
http://127.0.0.1:7860
```

## How the project works

```text
Farmer question
       ↓
Gradio UI
       ↓
Keyword retrieval
       ↓
Relevant scheme(s)
       ↓
Local knowledge base
       ↓
Optional Groq + Llama
       ↓
Simple answer
```

## Example

Question:

```text
I need crop insurance. Which scheme should I check?
```

The retrieval system matches words such as:

```text
crop + insurance
```

and finds:

```text
Pradhan Mantri Fasal Bima Yojana (PMFBY)
```

## Important limitation

This is a student/educational project. It does not decide legal eligibility,
submit applications, or guarantee benefits. Government scheme rules can
change, and state/district/crop/season conditions may apply.

## Official sources used in the initial knowledge base

PM-KISAN:
https://pmkisan.gov.in/

PMFBY:
https://pmfby.gov.in/

Kisan Credit Card:
https://www.myscheme.gov.in/schemes/kcc

Agriculture Infrastructure Fund:
https://agriinfra.dac.gov.in/

Soil Health Card:
https://soilhealth.dac.gov.in/

e-NAM:
https://www.enam.gov.in/

PMKSY:
https://pmksy.gov.in/
