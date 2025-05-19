import re
import requests
import random
from datetime import datetime

# -----------------------------
# Synthetic Data Generators
# -----------------------------
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
        hour = random.randint(0, 23)
        minute = random.randint(0, 59)
        return f"{hour:02d}:{minute:02d}"
    else:
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
    amount = random.uniform(0.5, 5000)
    if amount >= 1000:
        return f"${amount:,.2f}"
    else:
        return f"${amount:.2f}"

# -----------------------------
# Regex Extraction Functions
# -----------------------------
def extract_emails(text):
    """Extract email addresses from text."""
    return re.findall(r"[\w.-]+@[\w.-]+\.\w+", text)

def extract_urls(text):
    """Extract URLs from text."""
    return re.findall(r"https?://[\w.-]+(?:\.[\w.-]+)+(?:/[\w\-._~:/?#[\]@!$&'()*+,;=]*)?", text)

def extract_phone_numbers(text):
    """Extract phone numbers in various formats from text."""
    return re.findall(r"(?:\(\d{3}\)|\d{3})[-.\s]?\d{3}[-.\s]?\d{4}", text)

def extract_credit_cards(text):
    """Extract credit card numbers from text."""
    return re.findall(r"(?:\d{4}[- ]?){3}\d{4}", text)

def extract_times(text):
    """Extract times in 24-hour and 12-hour formats from text."""
    return re.findall(r"(?:[01]?\d|2[0-3]):[0-5]\d(?:\s?(?:AM|PM|am|pm))?", text)

def extract_html_tags(text):
    """Extract HTML tags from text."""
    return re.findall(r"<[^>]+>", text)

def extract_hashtags(text):
    """Extract hashtags from text."""
    return re.findall(r"#[A-Za-z0-9_]+", text)

def extract_currency(text):
    """Extract currency amounts (e.g., $19.99, $1,234.56) from text."""
    return re.findall(r"\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?", text)

# -----------------------------
# Main Extraction Logic
# -----------------------------
def fetch_and_generate_data(num_users=50):
    """Fetch user data from API and generate synthetic fields."""
    print("Fetching data from Random User API...")
    response = requests.get(f"https://randomuser.me/api/?results={num_users}")
    data = response.json()
    text_blob = ""
    for user in data["results"]:
        email = user["email"]
        phone = user["phone"]
        cell = user["cell"]
        url = user["picture"]["large"]
        text_blob += f"{email}\n{phone}\n{cell}\n{url}\n"
        text_blob += f"{generate_credit_card()}\n"
        text_blob += f"{generate_time()}\n"
        text_blob += f"{generate_html_tag()}\n"
        text_blob += f"{generate_hashtag()}\n"
        text_blob += f"{generate_currency()}\n"
    return text_blob

def extract_all(text):
    """Extract all supported data types from text."""
    return {
        "Emails": sorted(set(extract_emails(text))),
        "URLs": sorted(set(extract_urls(text))),
        "Phone Numbers": sorted(set(extract_phone_numbers(text))),
        "Credit Card Numbers": sorted(set(extract_credit_cards(text))),
        "Times": sorted(set(extract_times(text))),
        "HTML Tags": sorted(set(extract_html_tags(text))),
        "Hashtags": sorted(set(extract_hashtags(text))),
        "Currency Amounts": sorted(set(extract_currency(text))),
    }

def write_output(results, filename="output.txt"):
    """Write extracted results to a file in a grouped format."""
    with open(filename, "w", encoding="utf-8") as f:
        for key, values in results.items():
            f.write(f"{key}:\n")
            for v in values:
                f.write(f"  {v}\n")
            f.write("\n")
    print(f"Extraction complete. Results written to {filename}.")

# -----------------------------
# Entry Point
# -----------------------------
def main():
    text_blob = fetch_and_generate_data(num_users=50)
    results = extract_all(text_blob)
    write_output(results, filename="output.txt")

if __name__ == "__main__":
    main()