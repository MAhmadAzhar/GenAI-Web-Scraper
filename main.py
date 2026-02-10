import requests
from Db import create_tables, get_connection
from Ai_extractor import extract_jobs

URL = "https://www.python.org/jobs/"

def main():
    # 1. Make sure table exists
    create_tables()

    # 2. Fetch HTML
    response = requests.get(URL)
    response.raise_for_status()
    html = response.text

    # 3. Extract job data via GenAI
    jobs = extract_jobs(html)

    # 4. Insert into MySQL
    conn = get_connection()
    cursor = conn.cursor()

    for job in jobs:
        cursor.execute(
            "INSERT INTO jobs (name, client, looking_for, posted_on, categories) VALUES (%s, %s, %s, %s, %s)",
            (
                job.get("name"),
                job.get("client"),
                ", ".join(job.get("looking_for", [])),
                job.get("posted_on"),
                ", ".join(job.get("categories", []))
            )
        )

    conn.commit()
    conn.close()

    print(f"{len(jobs)} jobs inserted into MySQL database")

if __name__ == "__main__":
    main()
