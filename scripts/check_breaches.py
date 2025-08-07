import csv
import requests
import time
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get the API key
API_KEY = os.getenv("HIBP_API_KEY")
print(f"DEBUG: Loaded API key = {API_KEY}")

# Email addresses to check (grouped by organization)
EMAILS_TO_CHECK = [
    # Adams State University
    "admin@adams.edu",
    "webmaster@adams.edu",

    # San Luis Valley Medical Center / SLV Health
    "admin@slvhealth.org",
    "info@slvhealth.org",
    "adsn@slvhealth.org",

    # Alamosa County
    "admin@alamosacounty.org",
    "web@alamosacounty.org",
    "it@alamosacounty.org",

    # City of Alamosa
    "info@ci.alamosa.co.us",
    "webmaster@ci.alamosa.co.us",

    # Conejos County Hospital
    "it@conejoshospital.org",
    "admin@conejoshospital.org"
]

# Set up CSV output (without email column)
output_file = "../data/results.csv"
csv_file = open(output_file, mode="w", newline="", encoding="utf-8")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Breach Name", "Breach Date"])

headers = {
    "hibp-api-key": API_KEY,
    "User-Agent": "BreachChecker/1.0"
}

def check_email(email, retries=5):
    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}?truncateResponse=false"
    headers = {
        "hibp-api-key": API_KEY,
        "User-Agent": "BreachChecker/1.0"
    }

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            print(f"[!] Breaches found for {email}:")
            for breach in response.json():
                name = breach["Name"]
                date = breach["BreachDate"]
                print(f"  – {name} ({date})")
                csv_writer.writerow([email, name, date])

        elif response.status_code == 404:
            print(f"[✓] No breaches found for {email}")

        elif response.status_code == 429:
            if retries > 0:
                print(f"[!] Rate limit hit – retrying for {email}... ({retries} tries left)")
                time.sleep(7)
                return check_email(email, retries - 1)
            else:
                print(f"[✘] Rate limit exceeded for {email} – skipping")

        else:
            print(f"[✘] Error {response.status_code} for {email}")

    except Exception as e:
        print(f"[!] Exception for {email}: {e}")
# Run the checks
for email in EMAILS_TO_CHECK:
    check_email(email)
    time.sleep(1.5)

csv_file.close()
