import pandas as pd

# Load cleaned dataset
cleaned_data = pd.read_csv('data/cleaned_co2_data.csv')

def test_required_columns():
    # Check if all required columns are present
    required_columns = [
        'country', 'year', 'co2', 'coal_co2', 'oil_co2',
        'gas_co2', 'cement_co2', 'flaring_co2',
        'other_industry_co2', 'consumption_co2'
    ]

    # Ensure all required columns exist
    for col in required_columns:
        assert col in cleaned_data.columns, f"Required column '{col}' is missing."

    # Ensure no unexpected columns
    for col in cleaned_data.columns:
        assert col in required_columns, f"Unexpected column '{col}' is present."

def test_no_nulls():
    # Ensure there are no missing values in the cleaned dataset
    assert cleaned_data.isnull().sum().sum() == 0, "Null values are present in the dataset."

def test_no_duplicates():
    # Ensure there are no duplicate rows
    assert not cleaned_data.duplicated().any(), "Duplicate rows are present in the dataset."

# Run tests
test_required_columns()
print("test_required_columns passed.")

test_no_nulls()
print("test_no_nulls passed.")

test_no_duplicates()
print("test_no_duplicates passed.")
