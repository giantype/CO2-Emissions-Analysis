# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pycountry_convert as pc

# Manual corrections for unrecognised countries and regions
manual_country_to_continent = {
    "Cote d'Ivoire": "Africa",
    "Democratic Republic of Congo": "Africa",
    "Micronesia (country)": "Oceania",
    "Saint Helena": "Africa",
    "Curacao": "North America",
    "Kosovo": "Europe",
    "Sint Maarten (Dutch part)": "North America",
    "Bonaire Sint Eustatius and Saba": "North America",
    "Vatican": "Europe",
    "Ryukyu Islands": "Asia",
    "East Timor": "Asia",
    
    "Europe (excl. EU-27)": "Europe",
    "Europe (excl. EU-28)": "Europe",
    "European Union (27)": "Europe",
    "European Union (28)": "Europe",
    "North America (excl. USA)": "North America",
    "Asia (excl. China and India)": "Asia",
    
    "Africa (GCP)": "Africa",
    "Asia (GCP)": "Asia",
    "Europe (GCP)": "Europe",
    "North America (GCP)": "North America",
    "Oceania (GCP)": "Oceania",
    "South America (GCP)": "South America",
    "Central America (GCP)": "North America",

    "High-income countries": "Other",
    "Low-income countries": "Other",
    "Lower-middle-income countries": "Other",
    "Upper-middle-income countries": "Other",
    "World": "Other",
    
    "International aviation": "Other",
    "International shipping": "Other",
    "International transport": "Other",
    "Kuwaiti Oil Fires": "Other",
    "Kuwaiti Oil Fires (GCP)": "Other",
    "Ryukyu Islands (GCP)": "Asia",
    "Least developed countries (Jones et al.)": "Other",
    "Non-OECD (GCP)": "Other",
    "OECD (GCP)": "Other",
    "OECD (Jones et al.)": "Other",
    "Middle East (GCP)": "Asia",
}

# Continent mapping
def country_to_continent(country_name):
    
    if country_name in manual_country_to_continent:
        return manual_country_to_continent[country_name]

    try:
        country_code = pc.country_name_to_country_alpha2(country_name)
        continent_code = pc.country_alpha2_to_continent_code(country_code)
        continent_map = {
            'AF': 'Africa',
            'AS': 'Asia',
            'EU': 'Europe',
            'NA': 'North America',
            'SA': 'South America',
            'OC': 'Oceania'
        }
        return continent_map.get(continent_code, 'Other')
    except:
        return 'Other'


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

# Global CO2 emissions over time visual
global_emissions = data.groupby('year')['co2'].sum()
plt.figure(figsize=(12, 7))
plt.plot(global_emissions.index, global_emissions.values, marker='o', markersize=3, linestyle='-', color='orange', linewidth=2)
plt.title('Global CO₂ Emissions Over Time', fontsize=16, weight='bold')
plt.xlabel('Year', fontsize=14)
plt.ylabel('Total CO₂ Emissions (Million Tonnes)', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()

plt.savefig('Visualisations/global_co2_trend.png')

# CO₂ emissions by continent visual
continent_emissions = data.groupby(['year', 'country'])['co2'].sum().reset_index()
continent_emissions['continent'] = continent_emissions['country'].apply(country_to_continent)
continent_trend = continent_emissions.groupby(['year', 'continent'])['co2'].sum().unstack()

# exclude "other" category (the aggregated data was dominating the chart)
filtered_continent_trend = continent_trend.drop(columns='Other', errors='ignore')

custom_colors = {
    'Africa': '#1f77b4',         
    'Asia': '#ff7f0e',           
    'Europe': '#2ca02c',         
    'North America': '#9467bd',  
    'Oceania': '#d62728',        
    'South America': '#17becf'   
}

# Plot
plt.figure(figsize=(12, 7))
filtered_continent_trend.plot.area(ax=plt.gca(), stacked=True, color=[custom_colors[col] for col in filtered_continent_trend.columns], alpha=0.85, linewidth=0.5)
plt.title('CO₂ Emissions by Continent Over Time', fontsize=16, weight='bold')
plt.xlabel('Year', fontsize=14)
plt.ylabel('Total CO₂ Emissions (Million Tonnes)', fontsize=14)
plt.legend(title='Continent', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()

plt.savefig('Visualisations/continent_co2_trend.png')
plt.show()
