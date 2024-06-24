# A collection of popular health-related keywords

popular_health_keywords = [
    "fever",
    "cough",
    "headache",
    "diabetes",
    "hypertension",
    "depression",
    "anxiety",
    "vaccine",
    "exercise",
    "diet",
    "obesity",
    "cancer",
    "asthma",
    "cholesterol",
    "pain",
    "allergy",
    "flu",
    "cold",
    "arthritis",
    "infection",
    "pregnancy",
    "heart attack",
    "stroke",
    "surgery",
    "therapy",
    "medication",
    "virus",
    "bacteria",
    "nausea",
    "vomiting",
    "dizziness",
    "fatigue",
    "insomnia",
    "skin rash",
    "acne",
    "weight loss",
    "weight gain",
    "blood pressure",
    "heart disease",
    "back pain",
    "anemia",
    "thyroid",
    "hiv",
    "aids",
    "hepatitis",
    "viral",
    "bacterial",
    "inflammation",
    "mental health",
    "stress",
    "ulcer",
    "immunization",
    "contraception",
    "menstrual",
    "cramps",
    "menopause",
    "sexual health",
    "erectile dysfunction",
    "birth control",
    "hair loss",
    "migraine",
    "diarrhea",
    "constipation",
    "indigestion",
    "reflux",
    "osteoporosis",
    "muscle pain",
    "joint pain",
    "injury",
    "fracture",
    "first aid",
    "emergency",
    "addiction",
    "recovery",
    "rehabilitation",
    "nutrition",
    "vitamins",
    "minerals",
    "hydration",
    "dehydration",
    "sunburn",
    "heatstroke",
    "cold exposure",
    "immunity",
    "sore throat",
    "sinusitis",
    "bronchitis",
    "pneumonia",
    "tuberculosis",
    "malaria",
    "dengue",
    "chikungunya",
    "zika",
    "ebola",
    "sars",
    "covid-19",
    "testing",
    "diagnostic",
    "scan",
    "MRI",
    "ultrasound",
    "x-ray",
    "biopsy",
    "endoscopy",
    "colonoscopy",
    "blood test",
    "urine test",
    "allergy test",
    "sleep apnea",
    "snoring",
    "sleep disorders",
    "gerd",
    "lactose intolerance",
    "gluten intolerance",
    "food allergy",
    "eczema",
    "psoriasis",
    "dermatitis",
    "fungal infection",
    "ringworm",
    "chickenpox",
    "measles",
    "smallpox",
    "rabies",
    "lyme disease",
    "sepsis",
    "anaphylaxis",
    "poisoning",
    "toxicity",
    "overdose",
    "withdrawal",
    "autism",
    "down syndrome",
    "alzheimer's",
    "dementia",
    "parkinson's",
    "multiple sclerosis",
    "neurology",
    "stroke recovery",
    "paralysis",
    "speech therapy",
    "occupational therapy",
    "physical therapy",
    "chiropractic",
    "acupuncture",
    "massage",
    "yoga",
    "pilates",
    "cardio",
    "strength training",
    "aerobic",
    "anaerobic",
    "core exercises",
    "high blood sugar",
    "low blood sugar",
    "insulin",
    "metformin",
    "antibiotics",
    "antivirals",
    "antifungals",
    "antidepressants",
    "anxiolytics",
    "analgesics",
    "pain relievers",
    "nsaids",
    "corticosteroids",
    "hormone therapy",
    "chemotherapy",
    "radiation therapy",
    "surgical options",
    "laparoscopy",
    "amputation",
    "transplant",
    "kidney stones",
    "gallstones",
    "bladder infection",
    "uti",
    "incontinence",
    "prostate issues",
    "men's health",
    "women's health",
    "pediatric",
    "geriatric",
    "sports medicine",
    "orthopedics",
    "cardiology",
    "oncology",
    "endocrinology",
    "pulmonology",
    "gastroenterology",
    "dermatology",
    "neurology",
    "psychiatry",
    "psychology",
    "counseling",
    "wellness",
    "health insurance",
    "medicare",
    "medicaid",
    "insurance claim",
    "medical bill",
    "hospitalization",
    "clinic",
    "doctor",
    "nurse",
    "physician",
    "specialist",
    "appointment",
    "consultation",
    "second opinion",
    "telemedicine",
    "virtual health",
    "health app",
    "medical record",
    "e-prescription",
    "drug interactions",
    "side effects",
    "clinical trials",
    "research",
    "study",
    "breakthrough",
    "pandemic",
    "epidemic",
    "outbreak",
    "quarantine",
    "isolation",
    "sanitation",
    "hygiene",
    "disinfection",
    "handwashing",
    "face masks",
    "social distancing",
    "public health",
    "community health",
    "health policy",
    "healthcare system",
    "affordable care",
    "access to healthcare",
    "health disparity",
    "global health",
]


# This list can be used to match keywords in user queries
def check_keywords(query):
    found_keywords = [
        word for word in popular_health_keywords if word in query.lower()
    ]
    return len(found_keywords)