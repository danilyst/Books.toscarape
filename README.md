# ShopEasy Retail Intelligence – Web Scraping ETL Pipeline

## Project Overview

This project is a complete end-to-end web scraping ETL pipeline developed for the **ShopEasy Retail Intelligence** capstone project.

The pipeline extracts book product data from the educational website:

https://books.toscrape.com/

The extracted data is transformed, cleaned, and loaded into a PostgreSQL database for analytical and business intelligence purposes.

The project demonstrates practical implementation of:

- Web scraping
- Data cleaning
- ETL pipeline architecture
- PostgreSQL integration
- Logging and error handling
- Business analytics using SQL

---

# Business Problem

ShopEasy Retail Intelligence aims to monitor product pricing trends across online platforms.

The company currently faces challenges such as:

- Inconsistent pricing information
- Manual data collection
- Limited visibility into pricing trends
- Poor business decision-making

This project automates the data collection process and enables structured analytics for better insights.

---

# Project Objectives

The major objectives of this project are:

- Build a scalable web scraping pipeline
- Extract product data from a real-world website
- Clean and transform raw data
- Store structured data in PostgreSQL
- Generate business insights using SQL
- Implement ethical scraping practices

---

# Technologies Used

## Programming Language

- Python

## Libraries

- requests
- BeautifulSoup4
- pandas
- sqlalchemy
- psycopg2
- hashlib
- logging

## Database

- PostgreSQL

## Tools

- VS Code
- Git
- GitHub

---

# Project Structure

```text
Capstone_Project_Webscraping/
│
├── data/
│
├── logs/
│
├── python/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── pipeline.py
│   ├── logger.py
│   └── config.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ETL Pipeline Architecture

## 1. Extraction Phase

The extraction script:

- Scrapes data from 50 pages
- Extracts:
  - Book title
  - Price
  - Rating
  - Category
- Handles pagination
- Visits individual product pages to retrieve categories
- Uses request sessions for connection reuse
- Implements delays using `time.sleep()`
- Adds User-Agent headers
- Handles request failures and retries

### Extracted Fields

| Column | Description |
|---|---|
| book_id | Unique hash-generated identifier |
| title | Book title |
| category | Book category |
| price | Book price |
| rating | Book rating |

---

## 2. Transformation Phase

The transformation script performs:

### Data Cleaning

- Cleans corrupted price symbols
- Converts prices to numeric values
- Standardizes ratings
- Handles missing values
- Removes duplicate records
- Resets DataFrame indexes

### Data Validation

- Checks for null values
- Ensures data consistency
- Handles invalid records safely

---

## 3. Loading Phase

The cleaned data is loaded into PostgreSQL using SQLAlchemy.

### Database Features

- Structured PostgreSQL schema
- Primary key constraints
- Conflict handling using:
  
```sql
ON CONFLICT DO NOTHING
```

- Transaction management
- Logging integration

---

# PostgreSQL Data Model

```sql
CREATE SCHEMA IF NOT EXISTS bookstoscrape;

CREATE TABLE IF NOT EXISTS bookstoscrape.books (

    book_id TEXT PRIMARY KEY,

    title TEXT NOT NULL,

    category TEXT,

    price NUMERIC,

    rating FLOAT,

    loaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);
```

---

# Business Analytics

SQL queries were developed to answer important business questions such as:

## 1. Overpriced vs Underpriced Products

Identify products priced above or below category averages.

## 2. Price Variation by Category

Determine categories with inconsistent pricing behavior.

## 3. Price Trends Over Time

Track average prices across ETL runs.

## 4. Rating & Price Relationship

Analyze how ratings affect product pricing.

---

# Ethical Web Scraping Practices

This project follows responsible scraping standards by:

- Checking robots.txt rules
- Using User-Agent headers
- Implementing delays between requests
- Handling connection errors
- Avoiding server overload

---

# Logging & Error Handling

The project includes a centralized logging system that:

- Tracks ETL progress
- Captures extraction errors
- Logs transformation issues
- Monitors database loading

---

# Challenges Encountered

Some challenges encountered during development include:

- Connection reset errors
- DNS resolution failures
- Corrupted currency symbols
- Pagination handling
- Category extraction from nested pages

These were resolved through:

- Session reuse
- Retry handling
- Request delays
- Regex-based cleaning
- Improved exception handling

---

# Key Learnings

This project strengthened understanding of:

- Real-world web scraping
- ETL architecture
- Data transformation techniques
- PostgreSQL integration
- Logging and monitoring
- Business intelligence querying

---

# Future Improvements

Possible future enhancements include:

- Airflow scheduling
- Docker containerization
- Cloud database deployment
- Incremental loading
- Advanced retry mechanisms
- Dashboard visualization using Power BI or Tableau

---

# How to Run the Project

## 1. Clone Repository

```bash
git clone <repository_url>
```

---

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3. Configure PostgreSQL

Update database credentials in:

```python
config.py
```

---

## 4. Run ETL Pipeline

```bash
python pipeline.py
```

---

# Sample Outputs

The pipeline generates:

- Raw CSV data
- Cleaned CSV data
- PostgreSQL tables
- Log files
- SQL analytical outputs

---

