"""
Main execution script for the Inventory Data Extraction Pipeline.
This script orchestrates the process of extracting and processing inventory data from PDF files.
"""

import os
import sys
import json
import logging
from datetime import datetime
from typing import Dict, Any

from src.data_models import OwnerInfo, Inventory
from src.get_data import get_data_from_pdf
from src.preprocess_text import extract_data, align_content

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('pipeline.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

def validate_pdf_path(path: str) -> bool:
    """
    Validate if the provided path exists and is a PDF file.
    
    Args:
        path (str): Path to the PDF file
        
    Returns:
        bool: True if valid, False otherwise
    """
    if not os.path.exists(path):
        logger.error(f"File not found: {path}")
        return False
    if not path.lower().endswith('.pdf'):
        logger.error(f"File is not a PDF: {path}")
        return False
    return True

def process_inventory_pdf(pdf_path: str) -> Dict[str, Any]:
    """
    Process an inventory PDF file and extract structured data.
    
    Args:
        pdf_path (str): Path to the PDF file
        
    Returns:
        Dict[str, Any]: Extracted and processed data
        
    Raises:
        FileNotFoundError: If the PDF file doesn't exist
        ValueError: If the PDF content is invalid
        Exception: For other processing errors
    """
    try:
        logger.info(f"Starting to process PDF: {pdf_path}")
        
        # Extract text from PDF
        text = get_data_from_pdf(path=pdf_path)
        if not text:
            raise ValueError("No text content extracted from PDF")
        
        # Align content
        aligned_text = align_content(text)
        if not aligned_text:
            raise ValueError("Failed to align text content")
        
        # Extract and structure data
        processed_data = extract_data(text=aligned_text)
        if not processed_data:
            raise ValueError("Failed to extract structured data")
        
        logger.info("PDF processing completed successfully")
        return processed_data
        
    except FileNotFoundError as e:
        logger.error(f"File not found: {str(e)}")
        raise
    except ValueError as e:
        logger.error(f"Invalid PDF content: {str(e)}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error during processing: {str(e)}")
        raise

def save_output(data: Dict[str, Any], output_path: str = "output.json") -> None:
    """
    Save the processed data to a JSON file.
    
    Args:
        data (Dict[str, Any]): Processed data to save
        output_path (str): Path to save the output file
    """
    try:
        with open(output_path, "w") as f:
            json.dump(data, f, indent=4)
        logger.info(f"Output saved successfully to {output_path}")
    except Exception as e:
        logger.error(f"Failed to save output: {str(e)}")
        raise

def main():
    """Main execution function."""
    try:
        # Get PDF path from user
        pdf_path = input("Please enter the path to the inventory PDF: ").strip()
        
        # Validate PDF path
        if not validate_pdf_path(pdf_path):
            sys.exit(1)
        
        # Process the PDF
        processed_data = process_inventory_pdf(pdf_path)
        
        # Save the output
        save_output(processed_data)
        
        print("Inventory has been processed successfully!")
        
    except KeyboardInterrupt:
        logger.info("Process interrupted by user")
        print("\nProcess interrupted by user")
        sys.exit(0)
    except Exception as e:
        logger.error(f"Process failed: {str(e)}")
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()


