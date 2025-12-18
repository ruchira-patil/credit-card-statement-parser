# Credit Card Statement PDF Parser

## Objective
The goal of this project is to build a Python-based PDF parser that extracts key information from credit card statement PDFs across multiple credit card issuers. The solution is designed to handle real-world, text-based PDF statement formats.

---

## Features
- Parses credit card statement PDFs
- Supports multiple credit card issuers
- Extracts structured data using rule-based logic
- Easy to extend for additional banks or fields

---

## Supported Credit Card Issuers
- HDFC Bank  
- ICICI Bank  
- Axis Bank  
- SBI Card  
- American Express  

---

## Extracted Data Points
The parser extracts the following 5 key data points:
1. Credit Card Issuer  
2. Card Last 4 Digits  
3. Statement Period (Billing Cycle)  
4. Payment Due Date  
5. Total Amount Due  

---

## Tech Stack
- Python 3
- pdfplumber (PDF text extraction)
- Regular Expressions (pattern matching)

---

## Project Structure
credit_card_parser/
│
├── parser.py
├── README.md
└── samples/
├── sample.pdf
└── icici.pdf


---

## How It Works
1. The PDF file is read using the `pdfplumber` library.
2. Text is extracted from all pages of the statement.
3. The card issuer is detected based on keyword matching.
4. Regular expressions are applied to extract required data fields.
5. Extracted data is returned in a structured dictionary format.

---

## How to Run the Project

### 1. Install Dependencies
```bash
pip install pdfplumber
2. Place PDF File

Add a credit card statement PDF (text-based) inside the samples folder.

3. Update PDF Path

Edit the following line in parser.py if needed:

pdf_path = "samples/sample.pdf"

4. Run the Parser
python parser.py
