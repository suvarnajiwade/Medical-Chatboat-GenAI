import os
from pathlib import Path  # Path should be capitalized
import logging

# Setting up logging correctly
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# List of files to check/create
list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "app.py",
    "research/trials.ipynb"
]

# Iterating through the list of files
for filepath in list_of_files:
    filepath = Path(filepath)  # Use Path instead of path (Path is the correct class)
    filedir, filename = os.path.split(filepath)
    
    # Creating the directory if it doesn't exist
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")
    
    # Creating the file if it doesn't exist or if it's empty
    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        with open(filepath, "w"):
            logging.info(f"Creating empty file: {filepath}")
    
    # If file already exists
    else:
        logging.info(f"{filename} already exists")
