# alu_regex-data-extraction-uwenayoallain

## Regex Data Extraction - ALU Assignment

This project extracts various types of structured data from text files using Python and Regular Expressions (regex). It is designed to process large volumes of text and identify key data types for aggregation and analysis.

### Data Types Extracted
- **Email addresses** (e.g., user@example.com, firstname.lastname@company.co.uk)
- **URLs** (e.g., https://www.example.com, http://test-site.net)
- **Phone numbers** (formats like (123) 456-7890, 123-456-7890, 123.456.7890)
- **Credit card numbers** (formats like 1234 5678 9012 3456 or 1234-5678-9012-3456)
- **Time** (24-hour and 12-hour formats, e.g., 14:30, 2:30 PM)
- **HTML tags** (e.g., <p>, <div class="example">)
- **Hashtags** (e.g., #example, #ThisIsAHashtag)
- **Currency amounts** (e.g., $19.99, $1,234.56)

## Setup

1. Ensure you have Python 3.x installed.
2. Install the required package:
   ```bash
   pip install requests
   ```
3. Run the script:
   ```bash
   python main.py
   ```

## Usage
- The script fetches data from a public API and generates additional synthetic data.
- Extracted results are written to `output.txt` in the project directory.
- No input file is required.

## Output
- Results for each data type are grouped and listed in `output.txt`.

---