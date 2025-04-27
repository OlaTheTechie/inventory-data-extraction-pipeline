from src.data_models import OwnerInfo, Inventory
from src.get_data import get_data_from_pdf
from src.preprocess_text import extract_data, align_content
import re, json, pdfplumber
from datetime import datetime

# path = "data/home_inventory.pdf"

# text = get_data_from_pdf(path=path)

# aligned_text = align_content(text)

# preprocessed_text = extract_data(text=aligned_text)

# with open("output.json", "w") as f: 
#     json.dump(preprocessed_text, f, indent=4)



if __name__ == "__main__": 
    path = str(input("Please enter the path to the inventory pdf: "))

    text = get_data_from_pdf(path=path)

    aligned_text = align_content(text)

    preprocessed_text = extract_data(text=aligned_text)

    with open("output.json", "w") as f: 
        json.dump(preprocessed_text, f, indent=4)
    
    print("inventory has been processed successfully")


