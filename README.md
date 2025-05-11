# Telcom Data Ingestion with Incremental Processing on AWS Glue


This repository contains two AWS Glue PySpark ETL jobs designed to process telecom and customer subscription data from the AWS Glue Data Catalog. The jobs demonstrate how to load, transform, and analyze CSV data from Amazon S3 using Apache Spark on AWS Glue.

## Repository Structure

```
.
├── job1_process_file1.csv
├── job2_process_file2.csv
├── job3_process_file3.csv
├── process_customer_subscription_data.py
├── process_telcom_data_gds.py
└── README.md
```

## Scripts

### `process_customer_subscription_data.py`

- Loads data from the Glue table: `customer_subscription_2023_08_21_csv`
- Database: `telcom_catalog`
- Converts the dynamic frame to a Spark DataFrame
- Prints schema, displays sample rows, and prints the total number of records

### `process_telcom_data_gds.py`

- Loads data from the Glue table: `telcom_data_gds`
- Database: `telcom-in-catalog`
- Uses a transformation context: `s3_input_new`
- Includes proper Glue job initialization and commit handling

## Sample Data

The repo includes three sample CSV files:
- `job1_process_file1.csv`
- `job2_process_file2.csv`
- `job3_process_file3.csv`

These represent raw input data files that are assumed to be stored in S3 and cataloged in AWS Glue for ETL processing.

## How to Run

These jobs are intended to be run within the AWS Glue Job environment.

**Example Job Parameters (for Glue Console or CLI):**
```
--JOB_NAME process_customer_data_job
```

Ensure the corresponding Glue tables and S3 data locations are set up in your environment.

## Requirements

- AWS Glue (Job, Catalog, and Crawler setup)
- Python (PySpark environment managed by AWS Glue)
- AWS IAM Role with Glue and S3 permissions
- The datasets (`.csv` files) uploaded and cataloged in AWS Glue

## Output

The job logs will display:
- Data schema
- Sample data rows
- Row count

You can optionally extend these scripts to:
- Write processed data back to S3
- Filter with watermarks (for incremental loads)
- Join or aggregate data for analytics