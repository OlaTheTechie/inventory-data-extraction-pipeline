import re, pdfplumber, json
from datetime import datetime
from src.data_models import OwnerInfo, Inventory

def align_content(text: str): 
    for line in text: 
        line.strip()
        continue
    return text


def extract_data(text: str):

    # the regex patter to search for owner's info in th document
    owner_info_pattern = (
    r"Name\s+(?P<name>.+?)\n"
    r"Address\s+(?P<address>.+?)\n"
    r'City, Zip, Address\s*(?P<city_zip>.+?)\s*'
    r'Phone Number\s*(?P<phone>\(\d{3}\)\s*\d{3}-\d{4})'
    )

# the regex pattern to match each item in the document
    inventory_pattern = re.compile(r"""
        (?P<no>\d+)\s+                            
        (?P<area>[A-Za-z ]+)\s+                  
        (?P<item_description>[A-Za-z ]+)\s+       
        (?P<source>[A-Za-z ]+)\s+                  
        (?P<purchase_date>\d{2}/\d{2}/\d{4})\s+    
        (?P<style>[A-Za-z]+)\s+                   
        (?P<serial_no>[A-Za-z0-9]+)\s+    
        \$\s*(?P<value>[0-9,]+\.\d{2})        
        """, 
        re.VERBOSE
    )

    owner_match = re.search(owner_info_pattern, text, re.DOTALL)
    owner_details = list(owner_match.groups())

    owner = OwnerInfo(
        owner_name=owner_details[0], 
        owner_address=owner_details[1], 
        owner_telephone=owner_details[3]
    )

    inventories = []
    for match in inventory_pattern.finditer(text):
        inventory = match.groupdict()

        dt = datetime.strptime(inventory['purchase_date'], "%d/%m/%Y")
        inventory_object = Inventory(
            purchase_date=dt.isoformat(), 
            serial_number=inventory["serial_no"], 
            description=inventory["item_description"], 
            source_style=inventory["style"], 
            value=inventory["value"]
        )

        inventories.append(inventory_object)
        
    return {
        **owner.__dict__, 
        "data": [inventory.__dict__ for inventory in inventories]
    }
    