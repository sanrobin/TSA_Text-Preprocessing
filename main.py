import nltk
import string
import sys
import os
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from docx import Document
import PyPDF2

# Download necessary NLTK datasets
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Initialize the lemmatizer and stopwords
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

def extract_text_from_docx(file_path):
    """Extract text from Word document"""
    doc = Document(file_path)
    text = '\n'.join([paragraph.text for paragraph in doc.paragraphs])
    return text

def extract_text_from_pdf(file_path):
    """Extract text from PDF document"""
    text = ""
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"
    return text

def clean_text(text):
    """Clean and process text using NLP techniques"""
    # Tokenize the text
    tokens = word_tokenize(text)

    # Convert to lowercase and remove punctuation and stopwords
    tokens = [word.lower() for word in tokens if word.isalnum()]
    tokens = [word for word in tokens if word not in stop_words]

    # Lemmatize the words
    lemmatized_tokens = [lemmatizer.lemmatize(word) for word in tokens]

    # Join the tokens back into a single string
    cleaned_text = ' '.join(lemmatized_tokens)
    return cleaned_text

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <document_file>")
        print("Supported formats: .docx, .pdf")
        sys.exit(1)
    
    file_path = sys.argv[1]
    
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    
    # Extract text based on file extension
    file_ext = os.path.splitext(file_path)[1].lower()
    
    try:
        if file_ext == '.docx':
            text = extract_text_from_docx(file_path)
        elif file_ext == '.pdf':
            text = extract_text_from_pdf(file_path)
        else:
            print(f"Error: Unsupported file format '{file_ext}'. Supported formats: .docx, .pdf")
            sys.exit(1)
        
        # Clean the extracted text
        cleaned_text = clean_text(text)
        
        # Output results
        print(f"\nProcessed file: {file_path}")
        print(f"Original text length: {len(text)} characters")
        print(f"Cleaned text length: {len(cleaned_text)} characters")
        print("\n--- Cleaned Text ---")
        print(cleaned_text)
        
    except Exception as e:
        print(f"Error processing file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()