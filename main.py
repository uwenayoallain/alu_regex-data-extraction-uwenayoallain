import re
import requests
import random
from datetime import datetime, timedelta

# Helper functions to generate synthetic data

def generate_credit_card():
    """Generate a random credit card number in XXXX XXXX XXXX XXXX or XXXX-XXXX-XXXX-XXXX format."""
    nums = [str(random.randint(0, 9)) for _ in range(16)]
    if random.choice([True, False]):
        return '{} {} {} {}'.format(''.join(nums[:4]), ''.join(nums[4:8]), ''.join(nums[8:12]), ''.join(nums[12:]))
    else:
        return '{}-{}-{}-{}'.format(''.join(nums[:4]), ''.join(nums[4:8]), ''.join(nums[8:12]), ''.join(nums[12:]))

def generate_time():
    """Generate a random time in 12-hour or 24-hour format."""
    if random.choice([True, False]):
        # 24-hour format
        hour = random.randint(0, 23)
        minute = random.randint(0, 59)
        return f"{hour:02d}:{minute:02d}"
    else:
        # 12-hour format
        hour = random.randint(1, 12)
        minute = random.randint(0, 59)
        ampm = random.choice(["AM", "PM", "am", "pm"])
        return f"{hour}:{minute:02d} {ampm}"

def generate_html_tag():
    tags = [
        '<p>',
        '<div class="example">',
        '<img src="image.jpg" alt="description">',
        '<span>Sample</span>',
        '<a href="https://example.com">Link</a>'
    ]
    return random.choice(tags)

def generate_hashtag():
    words = ["example", "ThisIsAHashtag", "123abc", "PythonRocks", "AI2024"]
    return f"#{random.choice(words)}"

def generate_currency():
    # US dollars, with or without comma, always two decimals
    amount = random.uniform(0.5, 5000)
    if amount >= 1000:
        return f"${amount:,.2f}"
    else:
        return f"${amount:.2f}"

# Regex extraction functions

def extract_emails(text):
    """Extracts email addresses from text."""
    return re.findall(r"[\w.-]+@[\w.-]+\.\w+", text)

def extract_urls(text):
    """Extracts URLs from text."""
    return re.findall(r"https?://[\w.-]+(?:\.[\w.-]+)+(?:/[\w\-._~:/?#[\]@!$&'()*+,;=]*)?", text)

def extract_phone_numbers(text):
    """Extracts phone numbers in various formats from text."""
    return re.findall(r"(?:\(\d{3}\)|\d{3})[-.\s]?\d{3}[-.\s]?\d{4}", text)

def extract_credit_cards(text):
    """Extracts credit card numbers from text."""
    return re.findall(r"(?:\d{4}[- ]?){3}\d{4}", text)

def extract_times(text):
    """Extracts times in 24-hour and 12-hour formats from text."""
    # 24-hour: 14:30, 09:05; 12-hour: 2:30 PM, 11:59 am
    return re.findall(r"(?:[01]?\d|2[0-3]):[0-5]\d(?:\s?(?:AM|PM|am|pm))?", text)

def extract_html_tags(text):
    """Extracts HTML tags from text."""
    return re.findall(r"<[^>]+>", text)

def extract_hashtags(text):
    """Extracts hashtags from text."""
    return re.findall(r"#[A-Za-z0-9_]+", text)

def extract_currency(text):
    """Extracts currency amounts (e.g., $19.99, $1,234.56) from text."""
    return re.findall(r"\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?", text)

# Fetch data from Random User API
print("Fetching data from Random User API...")
response = requests.get("https://randomuser.me/api/?results=50")
data = response.json()

# Build a text blob with all fields
text_blob = ""
for user in data["results"]:
    email = user["email"]
    phone = user["phone"]
    cell = user["cell"]
    url = user["picture"]["large"]
    # Add all fields to the text blob
    text_blob += f"{email}\n{phone}\n{cell}\n{url}\n"
    # Add synthetic data
    text_blob += f"{generate_credit_card()}\n"
    text_blob += f"{generate_time()}\n"
    text_blob += f"{generate_html_tag()}\n"
    text_blob += f"{generate_hashtag()}\n"
    text_blob += f"{generate_currency()}\n"

# Extract and deduplicate/sort results
results = {
    "Emails": sorted(set(extract_emails(text_blob))),
    "URLs": sorted(set(extract_urls(text_blob))),
    "Phone Numbers": sorted(set(extract_phone_numbers(text_blob))),
    "Credit Card Numbers": sorted(set(extract_credit_cards(text_blob))),
    "Times": sorted(set(extract_times(text_blob))),
    "HTML Tags": sorted(set(extract_html_tags(text_blob))),
    "Hashtags": sorted(set(extract_hashtags(text_blob))),
    "Currency Amounts": sorted(set(extract_currency(text_blob))),
}

# Output results to output.txt
with open("output.txt", "w", encoding="utf-8") as f:
    for key, values in results.items():
        f.write(f"{key}:\n")
        for v in values:
            f.write(f"  {v}\n")
        f.write("\n")

print("Extraction complete. Results written to output.txt.")