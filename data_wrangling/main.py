```
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import argparse
import os

def read_data(file_path):
    """
    Reads the CSV file and returns a Pandas DataFrame.
    
    Parameters:
    file_path (str): The path to the CSV file.

    Returns:
    DataFrame: The data loaded into a DataFrame.
    """

def fill_missing_values(df):
    """
    Fills missing values in the DataFrame.

    - Fills the 'Age' column with the mean age.
    - Fills the 'Score' column with the median score.
    - Drops rows with missing 'Name' values.

    Parameters:
    df (DataFrame): The input DataFrame.

    Returns:
    DataFrame: The cleaned DataFrame.
    """
   

def normalize_score(df):
    """
    Normalizes the 'Score' column to a range of [0, 1].

    Parameters:
    df (DataFrame): The input DataFrame.

    Returns:
    DataFrame: The DataFrame with normalized 'Score'.
    """

def create_visualizations(df):
    """
    Creates and saves visualizations from the DataFrame.

    - A histogram of the 'Age' column.
    - A scatter plot of 'Age' vs 'Score'.
    - A correlation matrix heatmap.

    Parameters:
    df (DataFrame): The input DataFrame.
    """

def main(file_path):
    """
    Main function to run the data wrangling tasks.

    Parameters:
    file_path (str): The path to the CSV file.
    """
    df = read_data(file_path)
    df = fill_missing_values(df)
    df = normalize_score(df)
    create_visualizations(df)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Data Wrangling with Student Data')
    parser.add_argument('file_path', type=str, help='Path to the students_data.csv file')
    args = parser.parse_args()
    
    if os.path.exists(args.file_path):
        main(args.file_path)
    else:
        print(f"File {args.file_path} does not exist.")
```
