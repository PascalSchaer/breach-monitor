import requests
import os
import time
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get the API key
API_KEY = os.getenv("HIBP_API_KEY")
print(f"DEBUG: Loaded API key = {API_KEY}")

EMAILS_TO_CHECK = [
    # Adams State University
    "admin@adams.edu",
    "it@adams.edu",
    "webmaster@adams.edu",
    "president@adams.edu",

    # San Luis Valley Medical Center / SLV Health
    "admin@slvhospital.org",
    "info@slvhospital.org",
    "security@slvhospital.org",
    "admin@slvhealth.org",

    # Alamosa County
    "admin@alamosacounty.org",
    "it@alamosacounty.org",
    "clerk@alamosacounty.org",

    # City of Alamosa
    "info@ci.alamosa.co.us",
    "mayor@ci.alamosa.co.us",

    # Conejos County Hospital
    "it@conejoshospital.org",
    "admin@conejoshospital.org"
]

headers = {
    "hibp-api-key": API_KEY,
    "User-Agent": "BreachChecker/1.0"
}

def check_email(email):
    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}?truncateResponse=false"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print(f"[!] Breaches found for {email}:")
        for breach in response.json():
            print(f"    - {breach['Name']} ({breach['BreachDate']})")
    elif response.status_code == 404:
        print(f"[✓] No breaches found for {email}")
    elif response.status_code == 429:
        print(f"[!] Rate limit hit – waiting and retrying for {email}...")
        time.sleep(5)
        return check_email(email)
    else:
        print(f"[X] Error checking {email} – Status: {response.status_code}")

# Run the checks
for email in EMAILS_TO_CHECK:
    check_email(email)
    time.sleep(2)  # Respect rate limit
