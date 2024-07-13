This project uses Selenium and BeautifulSoup to scrape teacher information from the San Juan Unified School District staff directory.

## Description

The script navigates through the staff directory, extracts teacher names, titles, locations, and email addresses, and stores the data in a CSV file. The directory has multiple pages, and the script iterates through them to collect data.

## Requirements

- Python 3.x
- Selenium
- BeautifulSoup4
- pandas
- webdriver-manager

Additionally, this repository includes a file named `school_data_subset.csv` containing government data about every school in California. This file provides information about each school's address, type, and other relevant details.
