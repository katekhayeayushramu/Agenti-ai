# schemes.py
# Knowledge base for the Agricultural Government Scheme Information Agent.
# Scheme details should be rechecked on official portals before real-world use.

SCHEMES = [
    {
        "name": "PM-KISAN Samman Nidhi",
        "short_name": "PM-KISAN",
        "category": "Income Support",
        "ministry": "Ministry of Agriculture and Farmers Welfare",
        "purpose": "Provides income support to eligible landholding farmer families.",
        "benefits": "₹6,000 per year in three equal installments of ₹2,000, transferred to eligible beneficiaries' bank accounts, subject to scheme rules.",
        "eligibility": "Eligible landholding farmer families identified by the State/UT administration under PM-KISAN guidelines. The scheme has exclusion categories, so the agent should not promise eligibility.",
        "documents": ["Aadhaar", "Land/land-record details", "Bank account details", "Mobile number"],
        "application": "Use the official PM-KISAN portal and the applicable State/UT process. eKYC is mandatory for registered farmers.",
        "official_url": "https://pmkisan.gov.in/",
        "keywords": ["pm kisan", "pm-kisan", "kisan samman nidhi", "6000", "income support", "installment", "farmer money"]
    },
    {
        "name": "Pradhan Mantri Fasal Bima Yojana",
        "short_name": "PMFBY",
        "category": "Crop Insurance",
        "ministry": "Ministry of Agriculture and Farmers Welfare",
        "purpose": "Provides crop-insurance protection against covered crop losses and unforeseen events under notified conditions.",
        "benefits": "Financial support for admissible crop losses under the notified crop, area, season and risk provisions. The portal also provides application, premium, policy-status and grievance services.",
        "eligibility": "Farmers cultivating notified crops in notified areas may be covered subject to the applicable PMFBY rules. Coverage depends on state, district, crop and season notifications.",
        "documents": ["Farmer identity details", "Land/cultivation records as applicable", "Bank account details", "Crop and season details", "Documents required by the applicable process"],
        "application": "Use the official PMFBY portal/Farmer Corner or the applicable bank/insurance channel. Check the current state, district, crop and season notification before applying.",
        "official_url": "https://pmfby.gov.in/",
        "keywords": ["pmfby", "fasal bima", "crop insurance", "crop damage", "crop loss", "insurance", "natural calamity"]
    },
    {
        "name": "Kisan Credit Card",
        "short_name": "KCC",
        "category": "Agricultural Credit",
        "ministry": "Government of India / participating banks",
        "purpose": "Provides adequate and timely credit support for farmers' cultivation and eligible agriculture/allied needs.",
        "benefits": "A single-window credit facility can support cultivation, post-harvest expenses, produce marketing, working capital for farm assets/allied activities and eligible investment needs. Interest support may apply according to current rules.",
        "eligibility": "The official myScheme entry lists owner cultivators, tenant farmers, oral lessees, sharecroppers and eligible SHGs/JLGs of farmers among the eligible categories, subject to bank requirements.",
        "documents": ["Application form", "Photograph", "Identity proof", "Address proof", "Certified landholding/cultivation proof", "Other bank-required documents"],
        "application": "Apply through a participating bank, using its online or offline application process. The bank checks documents and eligibility under applicable rules.",
        "official_url": "https://www.myscheme.gov.in/schemes/kcc",
        "keywords": ["kcc", "kisan credit card", "farmer loan", "agriculture loan", "farm credit", "credit card"]
    },
    {
        "name": "Agriculture Infrastructure Fund",
        "short_name": "AIF",
        "category": "Agricultural Infrastructure",
        "ministry": "Ministry of Agriculture and Farmers Welfare",
        "purpose": "Supports financing for viable post-harvest management infrastructure and community farming assets.",
        "benefits": "Provides a financing facility for eligible agriculture-infrastructure projects at farm-gate and aggregation points, subject to scheme guidelines and lending conditions.",
        "eligibility": "The scheme guidelines cover eligible beneficiaries/projects including farmers, Farmer Producer Organizations, Primary Agricultural Cooperative Societies, agriculture entrepreneurs, startups, APMCs and other eligible entities, subject to the guidelines.",
        "documents": ["Applicant identity details", "Project proposal/details", "Financial documents", "Land/asset documents where applicable", "Lender-required documents"],
        "application": "Use the prescribed AIF process and participating financial institutions. Project and lender eligibility must be checked before application.",
        "official_url": "https://agriinfra.dac.gov.in/",
        "keywords": ["aif", "agriculture infrastructure fund", "warehouse", "cold storage", "post harvest", "farm infrastructure", "infrastructure"]
    },
    {
        "name": "Soil Health Card Scheme",
        "short_name": "SHC",
        "category": "Soil & Farm Advisory",
        "ministry": "Ministry of Agriculture and Farmers Welfare",
        "purpose": "Provides soil-test-based information to help farmers understand soil nutrient status and fertilizer recommendations.",
        "benefits": "A Soil Health Card reports soil characteristics and nutrient status and provides recommendations intended to support balanced nutrient management.",
        "eligibility": "Farmers can use the Soil Health Card system/services for soil testing and recommendations according to the applicable state and programme arrangements.",
        "documents": ["Basic farmer details", "Farm/field details", "Location details as required by the soil-testing process"],
        "application": "Use the official Soil Health Card portal or the relevant agriculture department/soil-testing facility to understand the current process in your area.",
        "official_url": "https://soilhealth.dac.gov.in/",
        "keywords": ["soil health", "soil health card", "soil test", "fertilizer", "nutrient", "soil"]
    },
    {
        "name": "e-NAM",
        "short_name": "e-NAM",
        "category": "Agricultural Marketing",
        "ministry": "Ministry of Agriculture and Farmers Welfare",
        "purpose": "Provides an electronic trading platform intended to improve transparency and market access in agricultural commodity trading through participating markets.",
        "benefits": "Provides an online platform for price discovery, market information and trading-related services for participating agricultural markets and users.",
        "eligibility": "Participation depends on the applicable e-NAM/market arrangements and the user's role, such as farmer, trader or other market participant.",
        "documents": ["Identity details", "Bank details where required", "Produce/market details", "Registration information required by the applicable market"],
        "application": "Use the official e-NAM portal and follow the registration/market process applicable to the farmer and participating market.",
        "official_url": "https://www.enam.gov.in/",
        "keywords": ["enam", "e nam", "mandi", "market", "agricultural market", "sell crop", "crop price", "trading"]
    },
    {
        "name": "Pradhan Mantri Krishi Sinchayee Yojana",
        "short_name": "PMKSY",
        "category": "Irrigation & Water Management",
        "ministry": "Government of India / implementing departments",
        "purpose": "Supports irrigation and water-use efficiency objectives through programme components implemented by the concerned departments and states.",
        "benefits": "Support varies by PMKSY component and current state/programme guidelines; it can include activities related to irrigation development and water-use efficiency.",
        "eligibility": "Eligibility is component- and state-specific. Farmers should check the current notification and implementing department for their location.",
        "documents": ["Farmer identity details", "Land details", "Bank details where applicable", "Documents specified by the relevant component/state"],
        "application": "Check the relevant state agriculture/water/implementing department and current PMKSY component guidelines before applying.",
        "official_url": "https://pmksy.gov.in/",
        "keywords": ["pmksy", "irrigation", "water", "micro irrigation", "drip", "sprinkler", "sinchai"]
    },
]

CATEGORIES = sorted({s["category"] for s in SCHEMES})
