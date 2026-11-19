import json

logs = [
    {"level": "INFO", "message": "Program started"},
    {"level": "ERROR", "message": "File not found"},
    {"level": "WARNING", "message": "Low memory"},
    {"level": "INFO", "message": "Program running"},
    {"level": "ERROR", "message": "Invalid input"}
]

with open("logs.json", "w") as file:
    json.dump(logs, file, indent=4)

with open("logs.json", "r") as file:
    data = json.load(file)

count = {
    "INFO": 0,
    "WARNING": 0,
    "ERROR": 0
}

for log in data:
    level = log["level"]
    count[level] += 1

print("LOG FILE ANALYSIS")

for level, total in count.items():
    print(level, ":", total)