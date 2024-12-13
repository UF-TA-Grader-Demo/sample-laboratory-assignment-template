# sample-laboratory-assignment-template
Template repository for the Sample Laboratory Assignment on GitHub Classroom. This repository contains the starter files and instructions for completing the assignment. Students should clone this repository to create their own version, following the naming convention: sample-laboratory-assignment-&lt;username>.

# Data Exploration & Data Wrangling Laboratory

## Assignment Description
In this assignment, you will practice data exploration and wrangling techniques using Python. You will work with a dataset containing student details and perform various tasks such as reading and processing a CSV file, cleaning the data, transforming the data, and visualizing the data.


## Objectives
- Learn data cleaning and preprocessing techniques.
- Understand data normalization and data discretization.
- Develop skills to visualize data using Matplotlib.

## Instructions
1. **Read CSV File**
    - Use Pandas to read a CSV file named `students_data.csv`.

2. **Data Cleaning**
    - Handle missing values by filling them with appropriate statistics like mean, median, or mode.
    - Remove any rows containing obvious errors or inconsistencies.
    - Detect and remove outliers using statistical methods or visual inspection.

3. **Data Transformation**
    - Normalize numerical columns to have values between 0 and 1.
    - Create new columns based on existing columns (e.g., aggregate columns, calculated fields).
    - Discretize continuous columns into categorical bins.

4. **Data Visualization**
    - Generate a histogram for one of the numerical columns, such as "Age".
    - Create scatter plots to explore relationships between multiple columns.
    - Plot a correlation matrix to visualize the relationships between numerical columns.

5. **Generate Outputs**
    - Ensure that all visualizations are saved as image files (e.g., `age_histogram.png`, `age_salary_scatter.png`, `correlation_matrix.png`).

## Setup 

1. **Clone the Repository**
    ```bash
    git clone https://github.com/YOUR_USERNAME/data-exploration-wrangling.git
    cd data-exploration-wrangling
    ```

2. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    # OR using setup.py
    pip install .
    ```

3. **Place `students_data.csv` in the root directory.**

4. **Run the Script**
    ```bash
    python data_wrangling/main.py
    ```

## Functions
### data_wrangling/main.py
- read_data(file_path) - Reads the CSV file and returns a dataframe.
- fill_missing_values(df) - Handles missing values in the dataframe.
- normalize_score(df) - Normalizes the 'Score' column in the dataframe.
- create_visualizations(df) - Creates visualizations and saves them as image files.

### main.py
Here is an example main.py file template that you will use for the Data Exploration & Data Wrangling assignment. This file outlines the basic functionality expected from your implementation, including reading data from a CSV file, cleaning and transforming the data, and creating visualizations. While your actual code may differ significantly, this template should provide a solid starting point. The script will take a file path for a CSV input as a command-line argument, perform the necessary data processing and visualizations, and save the output images.
 
You will also need to ensure that your code works with Linux-based systems. The setup instructions include using a requirements.txt to manage dependencies, but you can opt for a Pipfile if you prefer to use pipenv.

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


## Deliverables
- A Python script named `data_wrangling/main.py` containing the implemented code.
- Visualizations saved as `age_histogram.png`, `age_score_scatter.png`, and `correlation_matrix.png`.


## Requirements
- Python 3.x
- Pandas
- Matplotlib
- NumPy

## Evaluating the Repository using Included Test Cases
We have provided test cases to evaluate your submission automatically. The tests cover various aspects of your implementation, such as reading the CSV file, filling missing values, normalizing scores, and creating visualizations.

**test_data_wrangling.py Python test script will be used to evaluate your code in the GitHub Classroom environment**

### How to Run Tests Locally

1. **Install Testing Dependencies**
    ```bash
   pip install pytest
    ```

2. **Run Tests**
    ```bash
    pytest
    ```
## Collaborators
This file should contain a pipe-separated list describing who you worked with and a small text description describing the nature of the collaboration. If you visited a website for inspiration, including the website. This information should be listed in three fields as in the example is below:

    Katherine Johnson | kj@nasa.gov | Helped me understand calculations
    Dorothy Vaughan | doro@dod.gov | Helped me with multiplexed time management
    Stackoverflow | https://stackoverflow.com | Helped me with Python test compilation

## Tags

When ready to submit, create a tag on your repository using `git tag` on the latest commit:

```bash
git tag v1.0
git push origin v1.0
```

## Bugs and Assumptions
- Mention any known bugs or limitations of your code.
- List any assumptions made during the development process.

## Grading

Grades will be assessed according to the following distribution:

### 80%: Correctness

- This will be assessed by giving your code a range of inputs and checking the output.
- Use the creation of tests to prove correctness.

### 20%: Documentation

- Your README file should fully explain your process for developing your code.
- All other commands should be well-documented.
