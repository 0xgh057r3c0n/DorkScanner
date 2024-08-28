# DorkScanner: This is a simple Python tool for performing Google searches using dorking queries.

## Description
This is a simple Python tool for performing Google searches using dorking queries. Dorking is a technique used to find sensitive information on the internet by utilizing specific search queries.

## Features
- Perform Google searches with custom dorking queries.
- Specify the number of results to return.
- Display the title and URL of each search result.

## Installation

1. Clone the repository or download the script.
2. Navigate to the directory where the script is located.
3. Install the required dependencies using pip:

- `pip install -r requirements.txt`

## Usage

1. Run the script:

- `python DorkScanner.py`

2. Enter a dorking query when prompted (e.g., site:example.com filetype:pdf).
3. Enter the number of results to return (optional, default=10).
4. View the search results displayed in the terminal.

## Example Dorking Queries

- `site:example.com filetype:pdf` - Find PDF files on the example.com domain.
- `inurl:admin` - Find URLs containing the word "admin".
- `intext:password` - Find pages containing the word "password".
- `filetype:docx` - Find Microsoft Word documents.

## Disclaimer

Use this tool responsibly and in accordance with Google's terms of service. Be cautious as dorking can reveal sensitive information. 
