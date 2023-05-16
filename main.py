from pdf_extractor import extract_text_from_pdf, save_text
from text_classifier import classify_text
from gpt_text_cleaner import clean_text

def main():
    # 1. Extract text from PDF
    pdf_path = 'your_pdf_path.pdf'
    output_folder = 'output'
    output_filename = 'extracted_text.txt'
    text = extract_text_from_pdf(pdf_path)
    save_text(text, output_folder, output_filename)

    # 2. Classify text
    classified_text = classify_text(output_folder, output_filename)

    # 3. Clean text with GPT
    cleaned_text = clean_text(classified_text)

    # Continue with your process...

if __name__ == "__main__":
    main()
