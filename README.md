# Job Market Data Pipeline

## Project Overview

This project is an end-to-end ETL pipeline that collects job market data from a public job board API, processes and analyzes the data, and stores the results in a SQLite database.

The goal is to identify the most in-demand technical skills across job postings and demonstrate Data Engineering best practices.

---

## Architecture

```text
Extract
   ↓
Transform
   ↓
Analyze
   ↓
Load
```

Pipeline flow:

```text
API
 ↓
jobs_raw.csv
 ↓
jobs_clean.csv
 ↓
skills_analysis.csv
 ↓
SQLite Database
```

---

## Project Structure

```text
job-market-data-pipeline/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── database/
│
├── logs/
│
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── analysis.py
│   ├── load.py
│   ├── pipeline.py
│   └── logger_config.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Technologies Used

- Python
- Pandas
- Requests
- SQLite
- Logging
- Git
- GitHub

---

## Features

### Data Extraction

- Collects job postings from a public API
- Extracts company, title, location, tags and descriptions

### Data Transformation

- Removes duplicates
- Handles missing values
- Standardizes data structure

### Skills Analysis

The pipeline analyzes demand for skills such as:

- Python
- SQL
- AWS
- Azure
- Docker
- Spark
- Databricks
- Snowflake
- Git
- PostgreSQL

### Data Loading

Stores processed datasets and analysis results in a SQLite database.

### Logging

Tracks each ETL step through a log file.

---

## Sample Results

| Skill | Count |
|---------|---------:|
| Git | 146 |
| AWS | 57 |
| Python | 35 |
| SQL | 25 |
| Azure | 16 |
| Databricks | 11 |
| Snowflake | 10 |

---

## Installation

```bash
git clone <repository-url>
cd job-market-data-pipeline

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```

---

## Run the Pipeline

```bash
python src/pipeline.py
```

---

## Skills Demonstrated

- ETL Development
- API Integration
- Data Cleaning
- Data Analysis
- SQLite Database Management
- Logging
- Python Programming
- Git Version Control

---

## Author

Alpha Diallo

Aspiring Data Engineer