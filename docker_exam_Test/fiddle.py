import json

with open("./logs/validated.json", "r") as f:
    validated = json.load(f)

print(validated)