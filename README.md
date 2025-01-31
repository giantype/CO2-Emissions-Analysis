# Analysing Global CO₂ Emissions

---

## 1. Overview

This repository contains an analysis of global carbon dioxide (CO₂) emissions, exploring historical trends, regional contributions, and sectoral impacts. The analysis utilises the **OWID CO₂ and Greenhouse Gas Emissions Dataset**, which compiles data from reliable sources such as the Global Carbon Project and the International Energy Agency.

The goal of this project is to investigate the hypothesis:  
> **"Global CO₂ emissions are primarily driven by a small number of high-emitting countries and energy-intensive sectors."**

By examining emission patterns over time, across regions, and by industrial sectors, this project aims to provide insights to guide targeted climate change mitigation strategies.

---

## 2. Project Structure
- **`.circleci/`**: Configuration files for CircleCI integration for testing.
- **`Visualisations/`**: Stores visualisations related to the analysis.
- **`tests/`**: Includes test files ran by CircleCI.
- **`data/`**: Dataset used for the analysis.
- **`scripts/`**: Scripts for data cleaning, data analysis, and creating visualisations.
- **`.gitignore`**: Specifies files to be ignored by Git.
- **`README.md`**: Project documentation.
- **`Statistics.txt`**: Descriptive statistics.
- **`requirements.txt`**: Lists Python dependencies needed to run the analysis.

---

## 3. Dataset

The dataset used is the **OWID CO₂ and Greenhouse Gas Emissions Dataset**.

- **Source:** [Our World in Data](https://github.com/owid/co2-data)  
- **Data Coverage:** Global CO₂ emissions by country, year, and sector.  
- **Pre-processing:**  
  - Removed unnecessary columns.  
  - Filled missing numeric values with zeros.  
  - Standardised country names.  
  - Removed ambiguous or grouped entries.  

---

## 4. How to Run
To run the analysis locally:
1. Clone repository:
   ```bash
   git clone https://github.com/giantype/CO2-Emissions-Analysis.git
   cd CO2-Emissions-Analysis
2. Install required dependencies from 'requrements.txt':
   ```bash
   pip install -r requirements.txt

4. Run data analysis script - 'data_analysis.py':
   ```bash
   python scripts/data_analysis.py

6. To execute test suite:
    ```bash
    pytest tests/

7. View the visualisations:

   Navigate inside the 'Visualisations/' folder.