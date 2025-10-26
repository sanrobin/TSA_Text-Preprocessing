# TSA_Text-Preprocessing
A project on "Text Cleaning and Pre-Processing Tool using NLTK" which is done on my third year in college.
## Document Text Cleaner
A Python tool that extracts and cleans text from Word documents (.docx) and PDF files using natural language processing techniques.
## Features

- Extract text from Word documents (.docx)
- Extract text from PDF files (.pdf)
- Text cleaning using NLTK:
  - Tokenization
  - Stopword removal
  - Lemmatization
  - Punctuation removal

## Installation

1. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the script with a document file as an argument:

```bash
python main.py <document_file>
```

### Examples

```bash
# Process a Word document
python main.py document.docx

# Process a PDF file
python main.py report.pdf
```

## Output

The tool will display:
- Original text length
- Cleaned text length
- The processed and cleaned text

## Supported File Formats

- `.docx` - Microsoft Word documents
- `.pdf` - PDF documents

## Requirements

- Python 3.6+
- See `requirements.txt` for package dependencies
