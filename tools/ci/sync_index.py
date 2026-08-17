# Script to sync index
import json
import os

RELEASE_DIR = "releases"

files = [
    f for f in os.listdir(RELEASE_DIR)
    if f.endswith(".json") and f not in ["index.json", "latest.json"]
]

versions = []

for f in sorted(files, reverse=True):
    with open(f"{RELEASE_DIR}/{f}") as file:
        data = json.load(file)

    versions.append({
        "version": data["version"],
        "file": f,
        "title": data["title"],
        "release_type": data["release_type"],
        "status": data["status"],
        "label": data.get("label", ""),
        "date": data["period"]["end"],
        "highlights": data.get("highlights", [])[:4]
    })

index = {
    "project": "VISAR Edge",
    "latest_version": versions[0]["version"] if versions else None,
    "total_releases": len(versions),
    "versions": versions
}

with open("releases/index.json", "w") as f:
    json.dump(index, f, indent=2)

with open("releases/latest.json", "w") as f:
    json.dump(versions[0], f, indent=2)

print("Index updated")