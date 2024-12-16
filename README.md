# Supermarket Sales

  <h3 align="center">Supermarket Sales</h3>

  <p align="center">
    This is a simple data processing pipeline that pulls data from the <a href="https://www.kaggle.com/datasets/aungpyaeap/supermarket-sales?resource=download">supermarket-sales data set</a> from the <a href="https://github.com/Kaggle/kaggle-api">Kaggle API</a>. The data is then transformed, loaded into a SQLite databse, and a report is generated from the data.
  </p>
</p>

### Table of Contents

1. [About This Project](#about-this-project)
1. [Virtual Environment setup](#virtual-environment-setup)
1. [Running Locally](running_locally)
1. [Testing](#testing)
1. [Kaggle](#kaggle)
1. [Pipeline Overview](#pipeline_overview)
1. [Database Schema](#database_schema)
1. [Report](#report)

## About This Project
The objective of this project is to design and implement a data pipeline that extracts data from Kaggle, transforms it into dimension and fact tables, and loads it into a SQLite database. Additionally, a report will need to be generated based on the dimension and fact tables created.

## Virtual Environment setup

```bash
# build a virtual environment to install your Python packages
python3 -m venv ./venv

# 'activate' the virtual environment for your project
# do this every time you start a new terminal and enter your project folder
source venv/bin/activate

# install your Python packages
pip3 install -r requirements.txt
```

To shut off your virtual environment, run `deactivate` at a terminal where you
have an active virtual environment.

## Running Locally

Make sure you have downloaded the API key and placed it in the correct location(see below).

To run the application in your local dev environment run:
```bash
python main.py
```

## Testing

To run tests first activate your virtual environment with `source venv/bin/activate`<br>
Then run `python3 -m pytest`

## Kaggle

You will need a Kaggle API key in order to run this pipeline.  
1. Register or sign in to Kaggle: https://www.kaggle.com/
1. In your profile go to settings -> Under the 'API' section 'Create New Token'
1. Once token is downloaded ensure it is in the local path `/.kaggle/kaggle.json`

Dataset URL: https://www.kaggle.com/datasets/aungpyaeap/supermarket-sales?resource=download

## Pipeline Overview

`data_extraction.py`: Calls the Kaggle API, and downloads the data into the `/data` directory 

`data_transformation.py`: Pulls the raw data file from `/data`, does some minor transformations, identifies and splits data into what will be the dact table(sales) and the dimension tables(customers & products).  These three data sets are then saved as files in the `/transform_data` directory.

`data_load.py`: This pulls the three files from the `/transform_data` directory and loads the data into a SQLite database, `supermarket_sales.db`.  

`generate_report.py`: This runs a query on the database to create a report that is then uploaded to the `outgoing/reports` directory.  

---Add pic here---

## Database Schema

---Add pic here---

## Report

The current report generated shows the total sales by branch and product line.  In future iterations this could be modified for a different report or to create multuiple reports depending on business needs.

Location of generated report: `outgoing/reports`

SQL query generating the report:
```sql
        SELECT 
            c.city,
            c.customer_type,
            p.product_line,
            SUM(s.total) AS total_sales,
            RANK() OVER (PARTITION BY c.city ORDER BY SUM(s.total) DESC) AS rank
        FROM 
            sales s
        JOIN 
            customers c ON s.customer_id = c.customer_id
        JOIN 
            products p ON s.product_id = p.product_id
        GROUP BY 
            c.city, c.customer_type, p.product_line
        ORDER BY 
            c.city, rank;
```