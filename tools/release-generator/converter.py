# Converter script for release generation
import os
import sys
import json
from datetime import datetime
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

commit_msg = sys.argv[1]

SYSTEM_PROMPT = """
You are VISAR Release Compiler.

Convert commit logs into STRICT VISAR JSON format.

Rules:
- Output ONLY valid JSON
- No markdown, no explanation
- Follow schema exactly
- Extract version, title, codename, summary
- Group into: added, improved, fixed, removed
- If missing data, use empty arrays
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": commit_msg}
    ]
)

data = json.loads(response.choices[0].message.content)

version = data["version"]

os.makedirs("releases", exist_ok=True)

file_path = f"releases/v{version}.json"

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

print("Release generated:", file_path)