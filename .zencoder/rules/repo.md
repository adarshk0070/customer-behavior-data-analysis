---
description: Repository Information Overview
alwaysApply: true
---

# Customer Behavior Data Analyst Portfolio Project

## Summary
A comprehensive end-to-end data analytics portfolio project simulating a real-world workflow. It involves data preparation with Python, analysis with SQL (PostgreSQL/MySQL/SQL Server), and visualization using Power BI. The project identifies customer trends, segments, and purchase drivers from retail data.

## Structure
The repository is flat, containing all project resources in the root directory:
- **Code**: Jupyter Notebook (`.ipynb`) for data processing and SQL scripts (`.sql`) for analysis.
- **Data**: Raw CSV dataset (`customer_shopping_behavior.csv`).
- **Visualization**: Power BI dashboard file (`.pbix`).
- **Documentation**: Project reports (`.pdf`, `.pptx`) and `README.md`.

## Language & Runtime
**Language**: Python, SQL
**Runtime**: Jupyter Notebook environment (Python)
**Databases Supported**: PostgreSQL, MySQL, Microsoft SQL Server
**Analysis Tool**: Power BI

## Dependencies
**Python Libraries**:
- `pandas` (Data manipulation)
- `sqlalchemy` (Database connection)
- `psycopg2-binary` (PostgreSQL adapter)
- `pymysql` (MySQL adapter)
- `pyodbc` (ODBC/SQL Server adapter)

## Build & Installation
The project is designed to be run interactively.

1. **Install Python Dependencies**:
   ```bash
   pip install pandas sqlalchemy psycopg2-binary pymysql pyodbc
   ```

2. **Data Loading (Python)**:
   - Open `Customer_Shopping_Behavior_Analysis.ipynb`.
   - Run cells to clean data and load it into your chosen SQL database.

3. **Analysis (SQL)**:
   - Execute queries in `customer_behavior_sql_queries.sql` against your populated database.

4. **Visualization**:
   - Open `customer_behavior_dashboard.pbix` in Microsoft Power BI Desktop.
   - Configure the data source to point to your database.

## Main Files
- `Customer_Shopping_Behavior_Analysis.ipynb`: Main Python workflow for data cleaning and SQL ingestion.
- `customer_behavior_sql_queries.sql`: SQL scripts for answering business questions (contains PostgreSQL-specific casting `::numeric`).
- `customer_shopping_behavior.csv`: Source dataset.
- `customer_behavior_dashboard.pbix`: Power BI dashboard file.
- `Business Problem Document.pdf`: Documentation of the business context.
