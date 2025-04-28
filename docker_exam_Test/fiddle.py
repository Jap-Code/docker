import json

with open('/app/logs/validated.json', 'r') as f:
    validated = json.load(f)

print(validated)