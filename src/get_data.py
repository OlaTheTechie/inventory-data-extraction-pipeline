import pdfplumber 


def get_data_from_pdf(path): 
    with pdfplumber.open(path) as pdf: 
        text = ""
        for page in pdf.pages: 
            text = text + page.extract_text()
    return text