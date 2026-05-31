import json
import sys
import os
import re

commit_msg = sys.argv[1]

# SIMPLE VERSION DETECTION
version_match = re.search(r"v(\d+\.\d+\.\d+\.\d+)", commit_msg)
version = version_match.group(1) if version_match else "0.0.0.0"

data = {
    "id": f"visar-edge-v{version}",
    "version": version,
    "build": version,
    "codename": "VISAR Release",
    "title": commit_msg,

    "release_type": "major",
    "status": "stable",

    "period": {
        "start": "",
        "end": "",
        "days": 0
    },

    "summary": commit_msg,

    "highlights": [],

    "metrics": {
        "features_added": 0,
        "improvements": 0,
        "fixes": 0,
        "removed": 0,
        "breaking_changes": 0,
        "known_issues": 0
    },

    "sections": [
        {
            "key": "added",
            "title": "Added",
            "items": []
        },
        {
            "key": "improved",
            "title": "Improved",
            "items": []
        },
        {
            "key": "fixed",
            "title": "Fixed",
            "items": []
        },
        {
            "key": "removed",
            "title": "Removed",
            "items": []
        }
    ],

    "source": {
        "input_type": "commit_log",
        "generated_by": "github_action"
    }
}

os.makedirs("releases", exist_ok=True)

file_path = f"releases/v{version}.json"

with open(file_path, "w") as f:
    json.dump(data, f, indent=2)

print("Generated:", file_path)
