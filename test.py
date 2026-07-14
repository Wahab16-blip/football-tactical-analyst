import json

with open("reports.json", "r") as f:
    data = json.load(f)

print(f"{len(data)} reports found")
print("Keys:", list(data[0].keys()))