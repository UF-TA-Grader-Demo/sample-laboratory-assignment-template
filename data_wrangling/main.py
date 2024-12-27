import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Function to read data from a CSV file
def read_data(file_path):
    return pd.read_csv(file_path)
  
# Function to fill missing values in the DataFrame
def fill_missing_values(df):
    df_copy = df.copy()
    df_copy['Age'] = df_copy['Age'].fillna(df_copy['Age'].mean())
    df_copy['Score'] = df_copy['Score'].fillna(df_copy['Score'].median())
    df_copy.dropna(subset=['Name'], inplace=True)
    return df_copy
  
# Function to normalize the 'Score' column in the DataFrame
def normalize_score(df):
    df_copy = df.copy()
    df_copy['Score'] = (df_copy['Score'] - df_copy['Score'].min()) / (df_copy['Score'].max() - df_copy['Score'].min())
    return df_copy
  
# Function to create visualizations from the DataFrame
def create_visualizations(df):
    df_copy = df.copy()

    df_copy['Age'].plot(kind='hist', title='Age Histogram')
    plt.savefig('age_histogram.png')
    plt.show()
    plt.clf()

    df_copy.plot(kind='scatter', x='Age', y='Score', title='Age vs Score')
    plt.savefig('age_score_scatter.png')
    plt.show()
    plt.clf()

    # Select only numeric columns for correlation matrix
    numeric_cols = df_copy.select_dtypes(include=[np.number])
    correlation_matrix = numeric_cols.corr()

    plt.matshow(correlation_matrix)
    plt.xticks(range(len(correlation_matrix.columns)), correlation_matrix.columns, rotation=90)
    plt.yticks(range(len(correlation_matrix.columns)), correlation_matrix.columns)
    plt.colorbar()
    plt.savefig('correlation_matrix.png')
    plt.show()
  
if __name__ == '__main__':
    file_path = 'students_data.csv'
    df = read_data(file_path)
    df = fill_missing_values(df)
    df = normalize_score(df)
    create_visualizations(df)
