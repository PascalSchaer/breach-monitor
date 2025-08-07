import csv
from pathlib import Path

PRIVATE = Path("../data/results_with_emails.csv")   # private, gitignored
FALLBACK = Path("../data/results.csv")              # if you used the public script
PUBLIC  = Path("../docs/results_public.csv")        # safe to publish

source = PRIVATE if PRIVATE.exists() else FALLBACK
if not source.exists():
    raise SystemExit(f"Source CSV not found: {source} (run your private or public checker first)")

with open(source, newline="", encoding="utf-8") as fin, \
     open(PUBLIC,  "w", newline="", encoding="utf-8") as fout:

    reader = csv.DictReader(fin)
    # Flexible: if an Email column exists, we ignore it
    fieldnames = [c for c in reader.fieldnames if c.lower() not in ("email",)]
    # Force header to exactly these two for consistency
    fieldnames = ["Breach Name", "Breach Date"]

    writer = csv.DictWriter(fout, fieldnames=fieldnames)
    writer.writeheader()

    for row in reader:
        writer.writerow({
            "Breach Name": row.get("Breach Name") or row.get("Name") or row.get("Breach"),
            "Breach Date": row.get("Breach Date") or row.get("Date"),
        })

print(f"✅ Wrote sanitized CSV to {PUBLIC}")
