import spacy
import pandas as pd
from collections import defaultdict

# Load spaCy's pre-trained model for Named Entity Recognition and dependency parsing
nlp = spacy.load("en_core_web_sm")

# Create dictionaries to track entities and relationships
entity_data = defaultdict(list)
relationships = defaultdict(list)

# Function to extract Named Entities and relationships
def extract_entities_and_relationships(text, row_index):
    doc = nlp(text)
    entity_pairs = []

    # Extract named entities
    for ent in doc.ents:
        entity_data[ent.label_].append(ent.text)

    # Extract relationships based on dependency parsing
    for ent1 in doc.ents:
        for ent2 in doc.ents:
            if ent1 != ent2 and ent1.text != ent2.text:
                if ent1.root.dep_ == "nsubj" and ent2.root.dep_ == "dobj":
                    relationship = f"{ent1.text} -> {ent2.text} (Subject -> Object)"
                    relationships[relationship].append(row_index)
                    entity_pairs.append((ent1.text, "Subject-Object", ent2.text))
                elif ent1.root.dep_ == "nsubj" and ent2.root.dep_ == "prep":
                    relationship = f"{ent1.text} -> {ent2.text} (Subject -> Preposition)"
                    relationships[relationship].append(row_index)
                    entity_pairs.append((ent1.text, "Subject-Preposition", ent2.text))

    return entity_pairs

# Process the dataset
def process_data(df):
    extracted_data = []

    for index, row in df.iterrows():
        text = row["Text"]
        if text:  # Ensure the row contains text
            entity_pairs = extract_entities_and_relationships(text, index)
            for sub, rel, obj in entity_pairs:
                extracted_data.append((index, sub, rel, obj))

    # Convert extracted data to DataFrame
    extracted_df = pd.DataFrame(extracted_data, columns=["Row", "Entity1", "Relationship", "Entity2"])
    
    # Save extracted relationships to a CSV file
    extracted_df.to_csv("output_with_entities_and_relationships.csv", index=False)
    print("Named Entities and Relationships extracted and saved successfully!")

# Load the dataset
file_path = r'c:/Users/yuenw/Documents/datathon/__pycache__/cleaned_risk data.xlsx'
df = pd.read_excel(file_path)

# Check if 'Text' column exists and process the data
if "Text" in df.columns:
    process_data(df)
else:
    print("❌ No 'Text' column found in the dataset. Please check your Excel file.")
