# CQI_Capstone

This is a Data Engineering capstone project completed as part of the Talent Path program. The repository demonstrates key concepts and practices in data engineering, including data ingestion, transformation, exploration, and visualization. The project leverages AWS Glue for ETL, Python scripts for data manipulation, and Jupyter notebooks for analysis and exploration.

---

## Table of Contents
- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Repository Structure](#repository-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Project](#running-the-project)
- [Key Components](#key-components)
  - [AWS Glue Jobs](#aws-glue-jobs)
  - [Lambda Functions](#lambda-functions)
  - [Python Scripts](#python-scripts)
  - [Jupyter Notebooks](#jupyter-notebooks)
- [Data Flow and Architecture](#data-flow-and-architecture)
- [Contributing](#contributing)
- [License](#license)

---

## Project Overview

The CQI_Capstone project focuses on building a scalable and reproducible data pipeline. It demonstrates:
- **Data Ingestion**: Reading data from AWS S3 buckets and PostgreSQL databases.
- **Data Transformation**: Cleaning, normalizing, and enriching data using AWS Glue and Python.
- **Data Analysis**: Exploring and visualizing data with Jupyter notebooks and Python libraries like Pandas, Matplotlib, and Seaborn.
- **Data Export**: Writing transformed data back to S3 or PostgreSQL.

---

## Technologies Used

- **AWS Glue**: For ETL processes, including data cleaning and transformation.
- **AWS Lambda**: For serverless orchestration of Glue jobs and crawlers.
- **PostgreSQL**: As a relational database for storing and querying data.
- **Python**: For scripts and notebooks, leveraging libraries such as Pandas, NumPy, and Boto3.
- **Jupyter Notebooks**: For data exploration and visualization.
- **Boto3**: For AWS service integration.

---

## Repository Structure

```
CQI_Capstone/
├── Glue Transformations/
│   ├── ta-g2.py
│   ├── ta-glue2.py
├── Lambda Functions/
│   ├── ta-crawler.py
│   ├── taCrawlerGlue.py
│   ├── taLambda2.py
├── Notebooks/
│   ├── DataExploration.ipynb
│   ├── DFtoCSV.ipynb
│   ├── DFtoSQL.ipynb
│   ├── SQLtoS3.ipynb
├── Python Scripts/
│   ├── data_exploration.py
│   ├── df_to_csv.py
│   ├── df_to_sql.py
│   ├── s3_bucket_creation.py
│   ├── sql_to_s3.py
└── README.md
```

- **Glue Transformations**: Contains scripts used in AWS Glue jobs for ETL processes.
- **Lambda Functions**: Serverless functions written in Python to orchestrate Glue jobs and crawlers.
- **Notebooks**: Jupyter notebooks for data exploration, analysis, and visualization.
- **Python Scripts**: Standalone Python scripts for various data engineering tasks.

---

## Getting Started

### Prerequisites

- Python 3.8+
- Jupyter Notebook or JupyterLab
- PostgreSQL
- AWS account with access to Glue and S3
- Required Python libraries (see `requirements.txt` or install directly in scripts)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Abbast/CQI_Capstone.git
   cd CQI_Capstone
   ```

2. **Install dependencies**:
   - Using `pip`:
     ```bash
     pip install -r requirements.txt
     ```
   - Using `conda` (if `environment.yml` is provided):
     ```bash
     conda env create -f environment.yml
     conda activate cqi_capstone
     ```

### Running the Project

- **Jupyter Notebooks**:
  Open JupyterLab or Jupyter Notebook and navigate to the `Notebooks/` directory to run the notebooks.

- **Python Scripts**:
  Run standalone Python scripts from the command line, e.g.:
  ```bash
  python Python\ Scripts/data_exploration.py
  ```

- **AWS Glue Jobs**:
  Deploy and run Glue jobs using the scripts in the `Glue Transformations/` folder.

- **Lambda Functions**:
  Upload the scripts in `Lambda Functions/` to AWS Lambda and configure triggers.

---

## Key Components

### AWS Glue Jobs

- **ta-g2.py**: Reads data from S3, cleans, and transforms it using PySpark and Pandas.
- **ta-glue2.py**: Automates field selection and transformation before exporting to S3.

### Lambda Functions

- **ta-crawler.py**: Starts an AWS Glue crawler to catalog data in S3.
- **taCrawlerGlue.py**: Triggers AWS Glue jobs programmatically.
- **taLambda2.py**: Orchestrates the execution of a specific Glue job.

### Python Scripts

- **data_exploration.py**: Performs exploratory data analysis on the ingested dataset.
- **df_to_csv.py**: Converts data to a cleaned CSV format.
- **df_to_sql.py**: Inserts data into a PostgreSQL database.
- **sql_to_s3.py**: Exports data from PostgreSQL to S3.
- **s3_bucket_creation.py**: Automates the creation of S3 buckets.

### Jupyter Notebooks

- **DataExploration.ipynb**: Summarizes the dataset and identifies missing values.
- **DFtoCSV.ipynb**: Demonstrates data cleaning and export to CSV.
- **DFtoSQL.ipynb**: Shows how to upload data to PostgreSQL.
- **SQLtoS3.ipynb**: Exports SQL data to an S3 bucket.

---

## Data Flow and Architecture

1. **Data Ingestion**:
   - Raw data is uploaded to S3 or read from local files.
   - AWS Glue crawlers catalog the data.

2. **Data Transformation**:
   - Glue jobs clean and transform data using PySpark.
   - Additional transformations are performed using Python scripts and Pandas.

3. **Data Storage**:
   - Transformed data is saved to PostgreSQL or exported back to S3.

4. **Exploration and Visualization**:
   - Jupyter notebooks analyze the cleaned data and generate insights.

---

## Contributing

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-branch-name
   ```
3. Make changes and commit:
   ```bash
   git commit -m "Description of changes"
   ```
4. Push to your fork and submit a pull request.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.
