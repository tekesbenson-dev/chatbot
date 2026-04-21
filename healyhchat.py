import pandas as pd

# Load your data
df = pd.read_csv("health_data.csv")

# Normalize column names (removes spaces + makes lowercase)
df.columns = df.columns.str.strip().str.lower()

print("Healthbot: Hello there, I am your health assistant bot. Ask me about any symptoms.")

while True:
    # Get user input
    user_text = input("\nYou: ").lower().strip()

    # Exit condition
    if user_text == "quit":
        print("Healthbot: Goodbye! Nice to have been of service to you. Have a healthy day!")
        break

    found_answer = False

    # Loop through dataframe rows
    for index, row in df.iterrows():
        symptom = str(row.get("symptom", "")).lower()
        response = row.get("response", "No response available")

        # Handle keywords safely
        keywords_raw = str(row.get("keywords", ""))
        keywords_list = [k.strip() for k in keywords_raw.lower().split(",") if k.strip()]

        # Matching logic
        if user_text in symptom or user_text in keywords_list:
            print("Healthbot:", response)
            found_answer = True
            break

    # If no match found
    if not found_answer:
        print("Healthbot: Sorry, I couldn't find information about that symptom.")