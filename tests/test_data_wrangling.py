import pytest
from data_wrangling.main import read_data, fill_missing_values, normalize_score, create_visualizations

@pytest.fixture
def sample_data():
    return read_data('students_data.csv')

def test_read_csv(sample_data):
    assert list(sample_data.columns) == ['StudentID', 'Name', 'Age', 'Gender', 'Score', 'Major', '[REDACTED]']

def test_fill_missing_values(sample_data):
    df_cleaned = fill_missing_values(sample_data)
    assert not df_cleaned['Age'].isnull().any()
    assert not df_cleaned['Score'].isnull().any()

def test_normalize_score(sample_data):
    df_cleaned = fill_missing_values(sample_data)
    df_normalized = normalize_score(df_cleaned)
    assert df_normalized['Score'].min() == 0
    assert df_normalized['Score'].max() == 1

def test_create_visualizations(sample_data):
    df_cleaned = fill_missing_values(sample_data)
    df_normalized = normalize_score(df_cleaned)
    create_visualizations(df_normalized)
    assert os.path.isfile('age_histogram.png')
    assert os.path.isfile('age_score_scatter.png')
    assert os.path.isfile('correlation_matrix.png')

@pytest.mark.run(order=1)
def test_environment_set_up():
    assert True  # Add any necessary environmental check here
    
@pytest.mark.run(order=2)
def test_csv_file_upload():
    assert os.path.isfile('students_data.csv')
