import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def read_data(file_path):
    return pd.read_csv(file_path)

def fill_missing_values(df):
    df['Age'].fillna(df['Age'].mean(), inplace=True)
    df['Score'].fillna(df['Score'].median(), inplace=True)
    df.dropna(subset=['Name'], inplace=True)
    return df

def normalize_score(df):
    df['Score'] = (df['Score'] - df['Score'].min()) / (df['Score'].max() - df['Score'].min())
    return df

def create_visualizations(df):
    df['Age'].plot(kind='hist', title='Age Histogram')
    plt.savefig('age_histogram.png')
    plt.clf()

    df.plot(kind='scatter', x='Age', y='Score', title='Age vs Score')
    plt.savefig('age_score_scatter.png')
    plt.clf()

    correlation_matrix = df.corr()
    plt.matshow(correlation_matrix)
    plt.xticks(range(len(correlation_matrix.columns)), correlation_matrix.columns)
    plt.yticks(range(len(correlation_matrix.columns)), correlation_matrix.columns)
    plt.colorbar()
    plt.savefig('correlation_matrix.png')


if __name__ == '__main__':
    file_path = 'students_data.csv'
    df = read_data(file_path)
    df = fill_missing_values(df)
    df = normalize_score(df)
    create_visualizations(df)
