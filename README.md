# ALU Regex Data Extraction

## Features
- Fetches sample user data from a public API (Random User API)
- Extracts:
  - Email addresses
  - URLs
  - Phone numbers
  - Credit card numbers
  - Times (12-hour and 24-hour)
  - HTML tags
  - Hashtags
  - Currency amounts
- Outputs results in a clean, grouped format

## Data Types Extracted
- **Email addresses** (e.g., user@example.com)
- **URLs** (e.g., https://www.example.com)
- **Phone numbers** (e.g., (123) 456-7890)
- **Credit card numbers** (e.g., 1234 5678 9012 3456)
- **Times** (e.g., 14:30, 2:30 PM)
- **HTML tags** (e.g., <div class="example">)
- **Hashtags** (e.g., #PythonRocks)
- **Currency amounts** (e.g., $1,234.56)

## Setup
1. Ensure you have Python 3.x installed.
2. Install dependencies:
   ```bash
   pip install requests
   ```
3. Run the script:
   ```bash
   python main.py
   ```

## Usage
- The script fetches and generates data, then extracts all supported data types using regex.
- Results are written to `output.txt` in the project directory.
- No input file is required(for now).

## Output
- The output file `output.txt` contains each data type grouped and listed in a readable format, e.g.:
  ```
  Emails:
    user@example.com
    ...
  URLs:
    https://www.example.com
    ...
  ...
---