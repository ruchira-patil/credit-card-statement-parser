import pdfplumber
import re

def extract_text(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

def detect_issuer(text):
    if "HDFC" in text.upper():
        return "HDFC Bank"
    elif "ICICI" in text.upper():
        return "ICICI Bank"
    elif "AXIS" in text.upper():
        return "Axis Bank"
    elif "SBI" in text.upper():
        return "SBI Card"
    elif "AMERICAN EXPRESS" in text.upper():
        return "American Express"
    return "Unknown"

def parse_common_fields(text):
    card_match = re.search(r'XXXX\s+XXXX\s+XXXX\s+(\d{4})', text)
    period_match = re.search(r'Statement Period:\s*(.*)', text)
    due_match = re.search(r'Payment Due Date:\s*(.*)', text)
    amount_match = re.search(r'Total Amount Due:\s*₹?([\d,]+\.\d{2})', text)

    return {
        "card_last_4": card_match.group(1) if card_match else None,
        "statement_period": period_match.group(1) if period_match else None,
        "payment_due_date": due_match.group(1) if due_match else None,
        "total_amount_due": amount_match.group(1) if amount_match else None
    }

# ---- MAIN ----
pdf_path = "samples/icici.pdf"
text = extract_text(pdf_path)

issuer = detect_issuer(text)
data = parse_common_fields(text)

result = {
    "issuer": issuer,
    **data
}

print("===== FINAL OUTPUT =====")
print(result)
