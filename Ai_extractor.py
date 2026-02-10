from openai import OpenAI
import json
import os
import re
from bs4 import BeautifulSoup

# OpenRouter Configuration
os.environ["OPENROUTER_API_KEY"] = "your key here!!!!"

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

# HTML Cleaner
def clean_html(html):
    soup = BeautifulSoup(html, "html.parser")

    # remove scripts & styles
    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()

    text = soup.get_text(separator=" ", strip=True)

    # reduce excessive whitespace
    text = re.sub(r"\s+", " ", text)
    return text


# GenAI Job Extractor
def extract_jobs(html, user_query=""):
    cleaned_html = clean_html(html)

    prompt = f"""
You are a DATA EXTRACTION ENGINE.

SOURCE WEBSITE:
https://www.python.org/jobs/

USER FILTER:
{user_query}

STRICT RULES (MANDATORY):
- Output ONLY valid JSON
- Output MUST be a JSON ARRAY
- NO explanations
- NO markdown
- NO extra text
- If nothing matches, return []

JSON FORMAT:
[
  {{
    "name": "",
    "client": "",
    "posted_on": "",
    "categories": []
  }}
]

WEBSITE TEXT:
{cleaned_html[:10000]}
"""

    try:
        response = client.chat.completions.create(
            model="meta-llama/llama-3.1-8b-instruct",
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )

        raw = response.choices[0].message.content.strip()

        # remove accidental markdown
        raw = re.sub(r"```json|```", "", raw).strip()

        # hard safety check
        if not raw.startswith("["):
            print("Model did not return JSON array")
            print(raw[:500])
            return []

        data = json.loads(raw)

        if not isinstance(data, list):
            print("JSON is not a list")
            return []

        return data

    except Exception as e:
        print("Invalid JSON returned by GenAI")
        print(e)
        return []
