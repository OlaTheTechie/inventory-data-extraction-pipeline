# Inventory Data Extraction Pipeline

A Python-based data pipeline for extracting and processing inventory information from PDF documents.

![Alt text](assets/data-extraction-1.jpg "Optional title")


## Features

- PDF text extraction and processing
- Structured data extraction for inventory items
- Owner information parsing
- ISO format date standardization
- JSON output generation

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd inventory-data-extraction-pipeline
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the main script:
```bash
python main.py
```

When prompted, enter the path to your inventory PDF file. The script will process the PDF and generate an `output.json` file containing the extracted data.

## Project Structure

```
inventory-data-extraction-pipeline/
├── src/
│   ├── data_models.py    # Data models for OwnerInfo and Inventory
│   ├── get_data.py      # PDF data extraction functions
│   └── preprocess_text.py # Text processing and data extraction
├── data/                # Sample data directory
├── main.py             # Main execution script
├── requirements.txt    # Project dependencies
└── README.md          # This file
```

## Output Format

The pipeline generates a JSON file with the following structure:
```json
{
    "owner_name": "...",
    "owner_address": "...",
    "owner_telephone": "...",
    "data": [
        {
            "purchase_date": "YYYY-MM-DDT00:00:00",
            "serial_number": "...",
            "description": "...",
            "source_style_area": "...",
            "value": "..."
        }
    ]
}
```

## Requirements

- Python 3.6+
- pdfplumber
- datetime

## License

MIT License 