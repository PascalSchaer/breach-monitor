# Breach Monitor

This project is a **real-world cybersecurity tool** designed to monitor public data breaches using the [Have I Been Pwned (HIBP) API](https://haveibeenpwned.com/API/v3). It checks a list of known email addresses (e.g., from local institutions) and reports if any have appeared in publicly disclosed breaches.

## Purpose

- Help identify publicly exposed credentials tied to local government, education, or healthcare institutions.
- Demonstrate practical skills in cybersecurity, automation, and ethical threat monitoring.
- Provide actionable intelligence for responsible disclosure and outreach.

## Features

- Checks multiple email addresses for breach history
- Uses environment variables to protect your API key
- Handles rate limiting and API errors
- Outputs detailed information about any breaches found

## How It Works

1. Add your HIBP API key to a `.env` file  
2. Add email addresses you want to check to the script  
3. Run the script using Python  
4. Breach info (if any) is printed to the terminal  

## Project Structure

breach-monitor/
├── data/ # (Optional) Store results here
├── notes/ # Research notes, future plans
├── scripts/ # Python scripts, including the main checker
├── .env # Your HIBP API key (NOT committed)
├── .gitignore # Ignores .env and temp files
├── README.md # You're reading it!

## Disclaimer
This project is for educational and responsible disclosure purposes only.
Do not use this tool to target or harass individuals or organizations.

## Future Improvements
Export results to .json or .csv

Add domain or paste checking

Support for automation/scheduling

## Author
Pascal Schaer – Cybersecurity student and researcher
GitHub: github.com/PascalSchaer