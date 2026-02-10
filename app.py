from flask import Flask, render_template, request
import mysql.connector
import requests
from bs4 import BeautifulSoup
import re

from Ai_extractor import extract_jobs

app = Flask(__name__)

# MySQL connection (XAMPP Server)
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="scraped_jobs"
)
cursor = db.cursor(dictionary=True)


@app.route("/", methods=["GET", "POST"])
def index():
    jobs = []

    if request.method == "POST":
        user_query = request.form.get("query", "")

        # Extract year from user query (e.g. 2025)
        year = None
        match = re.search(r"(20\d{2})", user_query)
        if match:
            year = match.group(1)

        # Scrape website
        url = "https://www.python.org/jobs/"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        html = str(soup)

        # GenAI extraction (still extracts all jobs)
        extracted_jobs = extract_jobs(html, user_query)

        # Store in DB (ignore duplicates)
        for job in extracted_jobs:
            categories = job.get("categories", [])

            # Convert string → list
            if isinstance(categories, str):
                categories = [c.strip() for c in categories.split(",")]

            cursor.execute(
                """
                INSERT INTO jobs (name, client, looking_for, posted_on, categories)
                VALUES (%s, %s, %s, %s, %s)
                """,
                (
                    job.get("name"),
                    job.get("client"),
                    "",
                    job.get("posted_on"),
                    ", ".join(categories)
                ),
            )
        db.commit()

        # FILTER RESULTS BY YEAR
        if year:
            cursor.execute(
                "SELECT * FROM jobs WHERE posted_on LIKE %s",
                (f"%{year}%",)
            )
        else:
            cursor.execute("SELECT * FROM jobs")

        jobs = cursor.fetchall()

    return render_template("index.html", products=jobs)


if __name__ == "__main__":
    app.run(debug=True)
