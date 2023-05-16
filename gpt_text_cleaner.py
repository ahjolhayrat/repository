import json
import openai

# Set your OpenAI API key
openai.api_key = 'your OpenAI API key'

# Load your JSON file
with open('example.json', 'r') as f:
    data = json.load(f)

# Process each section
for section_label, section_text in data.items():
    print(f"Processing section: {section_label}")

    # Remove the "Label" from the section label
    section_label = section_label[:-5]

    if section_label == "TitleAndAuthors":
        # Special handling for TitleAndAuthors
        prompt = f"Given the text: \"{section_text}\", please identify and separate the title and the authors of the paper."
    else:
        # Define the prompt for other sections
        prompt = f"This text is from the {section_label} section of a scientific paper: \"{section_text}\". Please clean this text by removing irrelevant information and keeping only the relevant details for the {section_label} section. Do not modify the text, just remove the irrelevant parts."

    # Generate the output
    response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=100)

    # Extract cleaned text from the GPT-3 response
    cleaned_text = response.choices[0].text.strip()

    print(f"Cleaned text for {section_label}: {cleaned_text}\n")
