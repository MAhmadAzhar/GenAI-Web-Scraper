📌 Project Overview



This project is a Generative AI–assisted web scraping system built using Python and Flask. It scrapes job listings from python.org/jobs, uses a GenAI model to intelligently extract and filter relevant job data based on user queries, and stores the results in a MySQL (XAMPP) database with a searchable web interface.



🚀 Key Features



* Web scraping using Requests \& BeautifulSoup



* Intelligent data extraction using Generative AI (LLM via OpenRouter)



* Search jobs by:



-> Year (e.g. 2025)



-> Job title / keywords



-> Categories (e.g. Lead, Backend, Data)



* Data stored and retrieved from MySQL



* User-friendly web interface built with Flask



🛠️ Tech Stack



* Python



* Flask



* Requests



* BeautifulSoup



* MySQL (XAMPP / MariaDB)



* Generative AI (LLM via OpenRouter API)



📂 Project Structure

Web\_Scrape\_GenAI/

│

├── app.py              # Flask web application

├── main.py             # Optional standalone scraping runner

├── ai\_extractor.py     # GenAI-based job extraction logic

├── db.py               # Database connection logic

├── templates/

│   └── index.html      # Web UI

├── requirements.txt

└── README.md



⚙️ How It Works



-> User enters a query (year, role, category, keywords)



-> Website HTML is scraped using BeautifulSoup



-> Cleaned HTML is sent to a Generative AI model



-> AI extracts structured job data in JSON format



-> Data is stored in MySQL



-> Flask filters and displays results dynamically



▶️ How to Run the Project

-> Setup Virtual Environment

python -m venv .venv

.venv\\Scripts\\activate



-> Install Dependencies

pip install -r requirements.txt



-> Start XAMPP



1. Start Apache
2. Start MySQL
3. Create database: scraped\_jobs
4. Create table: jobs



-> Run Flask App

python app.py



-> Open Browser

http://127.0.0.1:5000



🧪 Example Queries



-> Python jobs in 2025



-> Lead developer jobs



-> Backend jobs



-> AI engineer



📌 Why Generative AI?



While BeautifulSoup extracts raw HTML, Generative AI understands context, filters irrelevant data, and converts unstructured content into clean, structured JSON, making the scraping process smarter and more flexible.

