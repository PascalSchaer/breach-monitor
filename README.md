# Breach Monitor

Automated, ethical monitoring of publicly disclosed breaches using the Have I Been Pwned (HIBP) API.  
This tool checks a curated list of institutional emails, handles rate limits, and exports results for reporting.

## Purpose

This project is designed to identify publicly disclosed breaches involving emails from local government, education, or healthcare institutions.  
It demonstrates practical skills in cybersecurity, automation, and responsible monitoring, while producing actionable data for responsible disclosure.

The goal is to:
- Highlight potential security risks from past breaches.
- Provide sanitized public reports for transparency.
- Support responsible disclosure efforts to affected institutions.

## Features

- Checks multiple email addresses for breach history using the HIBP API.
- Keeps API keys secure through environment variables in a `.env` file.
- Handles rate limiting and API errors gracefully.
- Exports results to both a private dataset (with emails) and a sanitized public dataset.

## How It Works

1. A list of target email addresses is defined in the script.
2. The script queries the HIBP API for breach history.
3. Any breaches found are printed to the terminal and stored in a CSV file.
4. Private results (with emails) are kept locally and excluded from version control.
5. A sanitized public CSV can be generated for sharing.

## Public Sample Results

A redacted, public-friendly version of the breach data is available here:  
[docs/results_public.csv](docs/results_public.csv)

This file contains breach names and dates but no email addresses.

## Running the Public (Sanitized) Checker

1. Clone the repository:
git clone https://github.com/<your-username>/breach-monitor.git
cd breach-monitor

2. Install dependencies:
pip install -r requirements.txt

3.Create a .env file from the example:
# Windows
copy .env.example .env
# macOS/Linux
cp .env.example .env     

4. Add your HIBP API key to .env:
HIBP_API_KEY=your_api_key_here

5. Run the public script:
python scripts/check_breaches.py

6. Sanitize results from a private run (optional):
python scripts/sanitize_results.py

The sanitized CSV will be created at:
docs/results_public.csv

## Folder Structure
breach-monitor/
│
├── .git/                   # Git repository data
├── data/                   # Stores breach results
│   ├── results.csv         # Private results with emails (gitignored)
│   └── results_public.csv  # Sanitized public results
│
├── docs/                   # Public documentation and CSV samples
├── notes/                  # Research or planning notes (not tracked in code)
├── scripts/                # Python scripts
│   ├── check_private.py    # Checks emails, outputs private CSV
│   ├── check_public.py     # (optional) Public checker variant (emails redacted in output)
│   └── sanitize_results.py # Sanitizes private results into public CSV
│
├── .env                    # Private environment variables (gitignored)
├── .env.example            # Example environment variables file
├── .gitignore              # Git ignore rules (protects sensitive files)
├── README.md               # Project documentation

## Ethics and Legal Use

- This project uses only publicly disclosed breach metadata via Have I Been Pwned.
- It does not test credentials, attempt to access systems, or exploit vulnerabilities.
- All results in this repository are sanitized.
- For significant findings, responsible disclosure procedures should be followed.
- Do not use this tool to target or harass individuals or organizations.

## Future Improvements

- Export results in JSON format.
- Add domain-wide breach checks.
- Support automated scheduled runs.
- Integrate notification options (Slack/Discord/webhooks).

## Author

**Pascal Schaer** – Cybersecurity student and researcher  
GitHub: [github.com/PascalSchaer](https://github.com/PascalSchaer)
