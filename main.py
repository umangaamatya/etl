#!/usr/bin/env python3
"""
Main ETL Pipeline Orchestrator
"""

import sys
import os

# Add the project root to the path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from extract.execute import download_zip_file, extract_zip_file, fix_json_dict
from transform.transform import transform_data
from load.load import load_data

def run_etl_pipeline(extract_path):
    """
    Run the complete ETL pipeline
    
    Args:
        extract_path (str): Path for data extraction
    """
    try:
        print("=== Starting ETL Pipeline ===")
        
        # Extract
        print("1. Starting Extraction...")
        KAGGLE_URL = "https://www.kaggle.com/datasets/yamaerenay/spotify-dataset-19212020-600k-tracks?resource=download"
        zip_filename = download_zip_file(KAGGLE_URL, extract_path)
        extract_zip_file(zip_filename, extract_path)
        fix_json_dict(extract_path)
        print("✓ Extraction completed!")
        
        # Transform
        print("2. Starting Transformation...")
        # TODO: Implement transformation logic
        print("⚠ Transformation not yet implemented")
        
        # Load
        print("3. Starting Load...")
        # TODO: Implement loading logic
        print("⚠ Load not yet implemented")
        
        print("=== ETL Pipeline Completed ===")
        
    except Exception as e:
        print(f"ETL Pipeline Error: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <extract_path>")
        print("Example: python3 main.py /Users/amatyaumanga/Workspace/etl")
        sys.exit(1)
    
    extract_path = sys.argv[1]
    exit_code = run_etl_pipeline(extract_path)
    sys.exit(exit_code)
