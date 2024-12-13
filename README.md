# sample-laboratory-assignment-template
Template repository for the Sample Laboratory Assignment on GitHub Classroom. This repository contains the starter files and instructions for completing the assignment. Students should clone this repository to create their own version, following the naming convention: sample-laboratory-assignment-&lt;username>.

# Data Exploration & Data Wrangling Laboratory


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

## Deliverables
- A Python script named `data_wrangling/main.py` containing the implemented code.
- Visualizations saved as `age_histogram.png`, `age_score_scatter.png`, and `correlation_matrix.png`.


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

## Requirements
- Python 3.x
- Pandas
- Matplotlib
- NumPy
