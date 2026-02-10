import mysql.connector

def get_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",        # your XAMPP MySQL username
        password="",        # your XAMPP MySQL password (empty by default)
        database="scraped_jobs"
    )
    return conn

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    # Table already created, so this is optional
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS jobs (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        client VARCHAR(255),
        looking_for TEXT,
        posted_on VARCHAR(50),
        categories TEXT
    )
    """)

    conn.commit()
    conn.close()
