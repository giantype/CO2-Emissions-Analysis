from pathlib import Path

statistics_file = Path('Statistics.txt')

def test_statistics_file_exists():
    # Check if Statistics.txt exists
    assert statistics_file.exists(), "Statistics.txt file is missing."

def test_statistics_file_not_empty():
    # Ensure Statistics.txt is not empty
    assert statistics_file.stat().st_size > 0, "Statistics.txt is empty."

def test_statistics_sections_exist():
    # Check if all statistical sections are included in the file
    with open(statistics_file, 'r', encoding='utf-8') as file:
        content = file.read()

    expected_sections = [
        "Global CO₂ Emissions Over Time Statistics:",
        "CO₂ Emissions by Continent Statistics:",
        "Top 10 CO₂ Emitting Countries",
        "CO₂ Emissions by Sector"
    ]

    for section in expected_sections:
        assert section in content, f"Section '{section}' is missing from Statistics.txt."

# Run tests
test_statistics_file_exists()
print("Statistics.txt file exists.")

test_statistics_file_not_empty()
print("Statistics.txt is not empty.")

test_statistics_sections_exist()
print("All expected sections are present in Statistics.txt.")
