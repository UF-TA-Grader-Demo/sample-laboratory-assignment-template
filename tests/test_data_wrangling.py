import unittest
import pandas as pd
from data_wrangling.main import read_data, fill_missing_values, normalize_score, create_visualizations

class TestDataWrangling(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.df = read_data('students_data.csv')

    def test_read_csv(self):
        self.assertEqual(list(self.df.columns), ['StudentID', 'Name', 'Age', 'Gender', 'Score', 'Major'])

    def test_fill_missing_values(self):
        df_cleaned = fill_missing_values(self.df)
        self.assertFalse(df_cleaned['Age'].isnull().any())
        self.assertFalse(df_cleaned['Score'].isnull().any())

    def test_normalize_score(self):
        df_normalized = normalize_score(self.df)
        self.assertTrue(df_normalized['Score'].min() == 0)
        self.assertTrue(df_normalized['Score'].max() == 1)

    def test_visualizations(self):
        df_cleaned = fill_missing_values(self.df)
        df_normalized = normalize_score(df_cleaned)
        create_visualizations(df_normalized)

if __name__ == '__main__':
    unittest.main()
