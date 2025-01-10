# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to clean data
def clean_data():
    # Load dataset
    data = pd.read_csv("data/owid-co2-data.csv")
    
    print("Shape of the data before cleaning:", data.shape)

    # Keep relevant columns
    required_columns = [
        'country', 'year', 'co2', 'coal_co2', 'oil_co2', 'gas_co2',
        'cement_co2', 'flaring_co2', 'other_industry_co2', 'consumption_co2'
    ]
    
    data = data[required_columns]

    # Handle missing values
    numeric_columns = [
        'co2', 'coal_co2', 'oil_co2', 'gas_co2',
        'cement_co2', 'flaring_co2', 'other_industry_co2', 'consumption_co2'
    ]

    # Fill missing numeric data with 0
    for col in numeric_columns:
        if col in data.columns:
            data[col] = data[col].fillna(0)

    # Fill missing country names with 'Unknown'
    data['country'] = data['country'].fillna('Unknown')

    # Drop rows with missing years
    data = data.dropna(subset=['year'])

    # Remove duplicates
    data = data.drop_duplicates()

    print("Shape of the data after cleaning:", data.shape)
    print("Missing values after cleaning:\n", data.isnull().sum())

    return data


data = clean_data()
print(data.head)
