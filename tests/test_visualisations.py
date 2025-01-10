from pathlib import Path

# Get path
visualisation_dir = Path('Visualisations')

# Expecetd files
expected_files = [
    'global_co2_trend.png',
    'continent_co2_trend.png',
    'top_10_countries_co2_bar.png',
    'sector_co2_bar_chart.png'
]

def test_files_exist():
    # Check if all expected visualization files exist
    for file_name in expected_files:
        file_path = visualisation_dir / file_name
        assert file_path.exists(), f"{file_name} is missing."

def test_files_not_empty():
    # Ensure all visualization files are not empty
    for file_name in expected_files:
        file_path = visualisation_dir / file_name
        assert file_path.stat().st_size > 0, f"{file_name} is empty."

# Run tests
test_files_exist()
print("All visualization files are present.")

test_files_not_empty()
print("All visualization files contain data.")
