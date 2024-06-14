"""# convertor/utils.py

import os
import pandas as pd
from PIL import Image

def read_csv(file_path):
    """
    #Reads a CSV file and returns a pandas DataFrame.
    #:param file_path: str - Path to the CSV file
    #:return: pd.DataFrame
"""
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except pd.errors.EmptyDataError:
        print(f"No data: {file_path}")
    except pd.errors.ParserError:
        print(f"Parsing error: {file_path}")
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    return None

def save_csv(df, file_path):
    """
    #Saves a pandas DataFrame to a CSV file.
    #:param df: pd.DataFrame - DataFrame to save
    #:param file_path: str - Path to save the CSV file
"""
    try:
        df.to_csv(file_path, index=False)
        print(f"File saved: {file_path}")
    except Exception as e:
        print(f"Error saving {file_path}: {e}")

def convert_image_to_grayscale(input_path, output_path):
    """
    #Converts an image to grayscale.
    #:param input_path: str - Path to the input image
    #:param output_path: str - Path to save the grayscale image
"""
    try:
        image = Image.open(input_path).convert('L')
        image.save(output_path)
        print(f"Image saved: {output_path}")
    except FileNotFoundError:
        print(f"File not found: {input_path}")
    except Exception as e:
        print(f"Error processing image {input_path}: {e}")

def resize_image(input_path, output_path, size):
    """
    #Resizes an image to the given size.
    #:param input_path: str - Path to the input image
    #:param output_path: str - Path to save the resized image
    #:param size: tuple - New size (width, height)
"""
    try:
        image = Image.open(input_path)
        image = image.resize(size, Image.ANTIALIAS)
        image.save(output_path)
        print(f"Image saved: {output_path}")
    except FileNotFoundError
    """