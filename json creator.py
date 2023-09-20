import json

# Create a dictionary with disease information
disease_info = {
    "Fungal Infection": {
        "Description": "Fungal infection is a common skin condition caused by various types of fungi.",
        "Precautions": ["Keep the affected area clean and dry.", "Use antifungal creams or medications as prescribed."],
        "Medications": ["Antifungal creams (e.g., clotrimazole)", "Oral antifungal medications (e.g., fluconazole)"]
    },
    "Allergy": {
        "Description": "Allergies occur when the immune system reacts to allergens, leading to symptoms like sneezing and itching.",
        "Precautions": ["Identify and avoid allergens.", "Take antihistamines as prescribed."],
        "Medications": ["Antihistamines (e.g., loratadine)", "Corticosteroids for severe allergies"]
    },
    "GERD (Gastroesophageal Reflux Disease)": {
        "Description": "GERD is a chronic condition where stomach acid flows back into the esophagus, causing heartburn and irritation.",
        "Precautions": [
            "Avoid trigger foods.",
            "Eat smaller meals.",
            "Maintain an upright posture after eating.",
            "Elevate the head of the bed."
        ],
        "Medications": ["Proton pump inhibitors (e.g., omeprazole)", "H2 blockers (e.g., ranitidine)"]
    },
    "Chronic Cholestasis": {
        "Description": "Chronic cholestasis is a liver condition where bile flow is obstructed, leading to a buildup of bile in the liver.",
        "Precautions": [
            "Treatment focuses on addressing the underlying cause, which may include surgery or medication."
        ],
        "Medications": []
    },
    "Drug Reaction": {
        "Description": "Drug reactions can range from mild skin rashes to severe allergic reactions caused by medications.",
        "Precautions": [
            "Take medications as prescribed.",
            "Be aware of potential side effects.",
            "Seek medical attention for severe reactions."
        ],
        "Medications": [
            "Treatment depends on the specific reaction and may include antihistamines, corticosteroids, or epinephrine."
        ]
    },
    "Peptic Ulcer Disease": {
        "Description": "Peptic ulcers are open sores that develop on the lining of the stomach, small intestine, or esophagus due to excessive stomach acid.",
        "Precautions": [
            "Avoid spicy and acidic foods.",
            "Limit alcohol and tobacco use.",
            "Take prescribed medications regularly."
        ],
        "Medications": ["Proton pump inhibitors (e.g., esomeprazole)", "Antibiotics (if caused by H. pylori infection)"]
    },
    "AIDS (Acquired Immunodeficiency Syndrome)": {
        "Description": "AIDS is a late stage of HIV infection where the immune system is severely damaged, making it difficult to fight off infections and diseases.",
        "Precautions": [
            "Practice safe sex.",
            "Use sterile needles for injections.",
            "Adhere to antiretroviral therapy (ART) as prescribed."
        ],
        "Medications": ["Antiretroviral drugs (e.g., tenofovir, efavirenz) to suppress HIV and slow down disease progression."]
    },
    "Diabetes": {
        "Description": "Diabetes is a chronic condition that affects how your body processes glucose (blood sugar). There are two main types, Type 1 and Type 2.",
        "Precautions": [
            "Monitor blood sugar levels.",
            "Maintain a balanced diet.",
            "Exercise regularly.",
            "Take medications or insulin as prescribed."
        ],
        "Medications": ["Insulin", "Oral medications (e.g., metformin)", "Other injectable drugs to manage blood sugar levels."]
    },
    "Gastroenteritis": {
        "Description": "Gastroenteritis, often referred to as stomach flu, is an inflammation of the stomach and intestines typically caused by viral or bacterial infections.",
        "Precautions": [
            "Stay hydrated.",
            "Rest.",
            "Practice good hygiene.",
            "Avoid contaminated food and water."
        ],
        "Medications": ["May include antidiarrheal medications (e.g., loperamide) and antiemetics (e.g., ondansetron) to manage symptoms."]
    },
    "Bronchial Asthma": {
        "Description": "Asthma is a chronic respiratory condition that causes airway inflammation and narrowing, leading to symptoms like wheezing and shortness of breath.",
        "Precautions": [
            "Identify triggers.",
            "Use inhalers as prescribed.",
            "Have an asthma action plan in case of exacerbations."
        ],
        "Medications": ["Bronchodilators (e.g., albuterol)", "Corticosteroids (e.g., fluticasone) to control inflammation."]
    },
    "Hypertension (High Blood Pressure)": {
        "Description": "Hypertension is a condition where blood pressure in the arteries is consistently elevated, increasing the risk of heart disease and stroke.",
        "Precautions": [
            "Maintain a low-sodium diet.",
            "Exercise regularly.",
            "Limit alcohol.",
            "Take prescribed antihypertensive medications."
        ],
        "Medications": ["Antihypertensive drugs (e.g., ACE inhibitors, beta-blockers) to lower blood pressure."]
    },
    "Migraine": {
        "Description": "Migraines are severe headaches often accompanied by other symptoms like nausea, vomiting, and sensitivity to light and sound.",
        "Precautions": [
            "Identify triggers.",
            "Manage stress.",
            "Use medications to prevent or relieve migraine attacks."
        ],
        "Medications": ["Triptans (e.g., sumatriptan)", "Preventive medications (e.g., topiramate) for chronic migraines."]
    },
    "Cervical Spondylosis": {
        "Description": "Cervical spondylosis is a degenerative condition of the cervical spine (neck) that can lead to neck pain and stiffness.",
        "Precautions": [
            "Maintain good posture.",
            "Perform neck exercises.",
            "Use supportive pillows."
        ],
        "Medications": ["Pain relievers (e.g., ibuprofen)", "Muscle relaxants", "Physical therapy for symptom management."]
    },
    "Paralysis (Brain Hemorrhage)": {
        "Description": "Paralysis often results from brain hemorrhage, causing loss of muscle function in specific body parts.",
        "Precautions": [
            "Rehabilitation therapy.",
            "Assistive devices.",
            "Medications to prevent complications and manage symptoms."
        ],
        "Medications": []
    },
    "Jaundice": {
        "Description": "Jaundice is a yellowing of the skin and eyes caused by the buildup of bilirubin in the blood, often due to liver or gallbladder problems.",
        "Precautions": [
            "Treat the underlying cause.",
            "Maintain hydration.",
            "Follow a low-fat diet."
        ],
        "Medications": ["Treatment depends on the underlying condition and may include antiviral drugs (for viral hepatitis) or surgery (for gallstones)."]
    },
    "Malaria": {
        "Description": "Malaria is a mosquito-borne infectious disease that causes fever, chills, and flu-like symptoms. It can be severe and life-threatening if left untreated.",
        "Precautions": [
            "Use insect repellents.",
            "Sleep under mosquito nets.",
            "Take antimalarial medications when traveling to endemic areas."
        ],
        "Medications": ["Antimalarial drugs (e.g., chloroquine, artemisinin-based combinations) for prevention and treatment."]
    },
        "Chickenpox": {
        "Description": "Chickenpox is a highly contagious viral infection characterized by an itchy rash, fever, and flu-like symptoms.",
        "Precautions": [
            "Isolate infected individuals.",
            "Avoid scratching the rash.",
            "Maintain good hygiene."
        ],
        "Medications": ["Antiviral medications (e.g., acyclovir) may be prescribed in severe cases."]
    },
    "Dengue": {
        "Description": "Dengue fever is a mosquito-borne viral illness that can cause high fever, severe joint and muscle pain, and potentially life-threatening complications.",
        "Precautions": [
            "Prevent mosquito bites with repellents and protective clothing.",
            "Seek medical care for symptoms."
        ],
        "Medications": ["Supportive care and fluid management for severe cases; no specific antiviral treatment."]
    },
    "Typhoid": {
        "Description": "Typhoid fever is a bacterial infection caused by Salmonella typhi, leading to high fever, abdominal pain, and gastrointestinal symptoms.",
        "Precautions": [
            "Practice good hygiene.",
            "Consume safe water and food.",
            "Consider typhoid vaccination when traveling to endemic areas."
        ],
        "Medications": ["Antibiotics (e.g., ciprofloxacin, azithromycin) to treat the infection."]
    },
    "Hepatitis A, B, C, D, E": {
        "Description": "Hepatitis viruses can cause inflammation of the liver, leading to various symptoms and potential long-term health issues.",
        "Precautions": [
            "Practice safe sex.",
            "Avoid sharing needles.",
            "Get vaccinated (for hepatitis A and B).",
            "Practice good hygiene."
        ],
        "Medications": ["Antiviral drugs (e.g., interferon, direct-acting antivirals) for hepatitis B and C; no specific treatment for hepatitis A, D, or E."]
    },
    "Alcoholic Hepatitis": {
        "Description": "Alcoholic hepatitis is liver inflammation caused by excessive alcohol consumption.",
        "Precautions": [
            "Abstain from alcohol.",
            "Seek medical care.",
            "Adopt a healthy lifestyle."
        ],
        "Medications": ["Treatment may include corticosteroids and nutritional support."]
    },
    "Tuberculosis (TB)": {
        "Description": "Tuberculosis is a bacterial infection that primarily affects the lungs, causing symptoms like cough, fever, and weight loss.",
        "Precautions": [
            "Complete the full course of TB medication.",
            "Practice respiratory hygiene.",
            "Get vaccinated if recommended."
        ],
        "Medications": ["Antibiotics (e.g., isoniazid, rifampin) for TB treatment."]
    },
    "Common Cold": {
        "Description": "The common cold is a viral respiratory infection characterized by a runny or stuffy nose, sore throat, and cough.",
        "Precautions": [
            "Practice good hand hygiene.",
            "Cover your mouth when sneezing or coughing.",
            "Get plenty of rest and fluids."
        ],
        "Medications": ["Over-the-counter cold remedies (e.g., decongestants, antihistamines) for symptom relief."]
    },
    "Pneumonia": {
        "Description": "Pneumonia is an infection that inflames the air sacs in the lungs, leading to symptoms like fever, cough, and difficulty breathing.",
        "Precautions": [
            "Vaccination (e.g., pneumococcal vaccine).",
            "Good hygiene.",
            "Prompt treatment for respiratory infections."
        ],
        "Medications": ["Antibiotics (e.g., amoxicillin, azithromycin) for bacterial pneumonia."]
    },
    "Dimorphic Hemorrhoids (Piles)": {
        "Description": "Piles or hemorrhoids are swollen veins in the rectum or anus, causing pain, bleeding, and discomfort.",
        "Precautions": [
            "Maintain a high-fiber diet.",
            "Stay hydrated.",
            "Avoid straining during bowel movements."
        ],
        "Medications": ["Over-the-counter creams, suppositories, or prescription medications for symptom relief."]
    },
    "Heart Attack": {
        "Description": "A heart attack occurs when blood flow to the heart muscle is blocked, leading to chest pain, shortness of breath, and other symptoms.",
        "Precautions": [
            "Adopt a heart-healthy lifestyle.",
            "Manage risk factors (e.g., high blood pressure, cholesterol).",
            "Seek emergency medical care for symptoms."
        ],
        "Medications": ["Medications such as aspirin, beta-blockers, and nitroglycerin may be used during and after a heart attack."]
    },
    "Varicose Veins": {
        "Description": "Varicose veins are swollen, twisted veins that often appear in the legs.",
        "Precautions": [
            "Elevate your legs.",
            "Wear compression stockings.",
            "Exercise regularly.",
            "Maintain a healthy weight."
        ],
        "Medications": ["Medications are typically not used to treat varicose veins; treatment options include procedures like sclerotherapy or laser therapy."]
    },
    "Hypothyroidism": {
        "Description": "Hypothyroidism is a condition where the thyroid gland doesn't produce enough thyroid hormone, leading to fatigue, weight gain, and other symptoms.",
        "Precautions": [
            "Take prescribed thyroid hormone replacement medication.",
            "Maintain regular follow-ups with your healthcare provider.",
            "Manage stress."
        ],
        "Medications": ["Levothyroxine is a common medication used to replace thyroid hormone."]
    },
    "Hyperthyroidism": {
        "Description": "Hyperthyroidism is a condition where the thyroid gland produces too much thyroid hormone, causing symptoms like rapid heartbeat and weight loss.",
        "Precautions": [
            "Follow your healthcare provider's treatment plan.",
            "Avoid excessive iodine intake.",
            "Manage stress."
        ],
        "Medications": ["Antithyroid drugs (e.g., methimazole, propylthiouracil) or radioactive iodine may be prescribed."]
    },
    "Hypoglycemia": {
        "Description": "Hypoglycemia is low blood sugar, which can cause symptoms like shakiness, confusion, and sweating.",
        "Precautions": [
            "Manage your blood sugar levels with a balanced diet.",
            "Have regular meals.",
            "Take medications (for diabetes)."
        ],
        "Medications": ["For severe hypoglycemia, glucagon or oral glucose tablets can be used."]
    },
    "Osteoarthritis": {
        "Description": "Osteoarthritis is a degenerative joint disease that leads to joint pain and stiffness.",
        "Precautions": [
            "Maintain a healthy weight.",
            "Engage in low-impact exercises.",
            "Protect your joints."
        ],
        "Medications": ["Pain relievers (e.g., acetaminophen, NSAIDs) and physical therapy can help manage symptoms."]
    },
     "Arthritis": {
        "Description": "Arthritis is an umbrella term for various joint inflammation conditions, with symptoms including joint pain and swelling.",
        "Precautions": [
            "Follow your healthcare provider's advice.",
            "Maintain a healthy lifestyle.",
            "Consider physical therapy."
        ],
        "Medications": [
            "Treatment varies by type but may include pain relievers, disease-modifying antirheumatic drugs (DMARDs), and biologics."
        ]
    },
    "(Vertigo) Paroxysmal Positional Vertigo": {
        "Description": "Vertigo is a sensation of spinning or dizziness. Paroxysmal positional vertigo is characterized by brief episodes of vertigo triggered by head movements.",
        "Precautions": [
            "Avoid rapid head movements that trigger vertigo.",
            "Follow vestibular rehabilitation exercises."
        ],
        "Medications": ["Medications are usually not the primary treatment; maneuvers to reposition displaced inner ear crystals are often performed."]
    },
    "Acne": {
        "Description": "Acne is a skin condition that causes pimples, blackheads, and whiteheads due to clogged pores.",
        "Precautions": [
            "Maintain good facial hygiene.",
            "Avoid picking or squeezing pimples.",
            "Use non-comedogenic skincare products."
        ],
        "Medications": [
            "Topical treatments (e.g., benzoyl peroxide, retinoids) and oral antibiotics may be prescribed for severe acne."
        ]
    },
    "Urinary Tract Infection (UTI)": {
        "Description": "UTI is a bacterial infection of the urinary system, causing symptoms like frequent urination and pain.",
        "Precautions": [
            "Stay hydrated.",
            "Urinate regularly.",
            "Practice good hygiene."
        ],
        "Medications": ["Antibiotics (e.g., trimethoprim-sulfamethoxazole, nitrofurantoin) are commonly used to treat UTIs."]
    },
    "Psoriasis": {
        "Description": "Psoriasis is a chronic skin condition that results in thickened, red, and scaly patches on the skin.",
        "Precautions": [
            "Moisturize the skin.",
            "Avoid triggers (e.g., stress).",
            "Use prescribed medications consistently."
        ],
        "Medications": [
            "Topical steroids, immunosuppressive drugs, and biologics may be prescribed, depending on the severity."
        ]
    },
    "Impetigo": {
        "Description": "Impetigo is a contagious skin infection characterized by red sores or blisters that break open and form a honey-colored crust.",
        "Precautions": [
            "Keep the affected area clean.",
            "Avoid close contact with others.",
            "Follow prescribed antibiotics."
        ],
        "Medications": ["Topical or oral antibiotics are used to treat impetigo."]
    }
}



# Specify the output JSON file path
json_file_path = "disease_info.json"

# Write the dictionary to a JSON file
with open(json_file_path, "w") as json_file:
    json.dump(disease_info, json_file, indent=4)

print(f"JSON file '{json_file_path}' created successfully.")
