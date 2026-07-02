# 🌍 EarthPulse-ETL

> **A Real-World Serverless ETL Pipeline with CI/CD on AWS**

![Python](https://img.shields.io/badge/Python-3.13-blue)
![AWS](https://img.shields.io/badge/AWS-Serverless-orange) ![GitHub
Actions](https://img.shields.io/badge/GitHub_Actions-CI-success)
![License](https://img.shields.io/badge/License-MIT-green)

## 📖 Overview

EarthPulse-ETL is a production-style serverless ETL pipeline that
extracts live earthquake data from the USGS API, uploads raw JSON to
Amazon S3, automatically triggers AWS Lambda, transforms and validates
records, and stores them in Amazon DynamoDB.

## ✨ Features

-   Extract live earthquake data
-   Upload raw JSON to Amazon S3
-   Event-driven AWS Lambda processing
-   Store validated records in DynamoDB
-   CloudWatch monitoring
-   GitHub Actions CI
-   AWS CodeBuild
-   AWS CodePipeline

## 🏗️ Architecture

``` text
USGS API
   │
Extract Script
   │
Raw JSON
   │
Amazon S3
   │
S3 Trigger
   ▼
AWS Lambda
   │
Transform
   ▼
Amazon DynamoDB
   │
CloudWatch

GitHub → GitHub Actions → CodePipeline → CodeBuild
```

## 🛠️ Tech Stack

-   Python 3.13
-   AWS Lambda
-   Amazon S3
-   DynamoDB
-   CloudWatch
-   IAM
-   boto3
-   GitHub Actions
-   AWS CodeBuild
-   AWS CodePipeline

## 📁 Project Structure

``` text
EarthPulse-ETL/
├── .github/workflows/
├── lambda/
├── sample_data/
├── scripts/
├── tests/
├── requirements.txt
├── buildspec.yml
└── README.md
```

## 🚀 Run Locally

``` bash
git clone https://github.com/tanmay-deev/EarthPulse-ETL.git
cd EarthPulse-ETL
python -m venv venv
pip install -r requirements.txt
aws configure
python scripts/run_pipeline.py
```

## 🔄 CI/CD

Every push to the `main` branch triggers:

1.  GitHub Actions validation
2.  AWS CodePipeline
3.  AWS CodeBuild

## ☁️ AWS Services

-   Amazon S3
-   AWS Lambda
-   Amazon DynamoDB
-   AWS IAM
-   Amazon CloudWatch
-   AWS CodePipeline
-   AWS CodeBuild
-   AWS CodeConnections

## 📸 Suggested Screenshots

-   GitHub Repository
-   GitHub Actions
-   CodePipeline
-   Lambda
-   CloudWatch
-   DynamoDB
-   Amazon S3
-   Folder Structure

## 👨‍💻 Author

**Tanmay Bonde**

GitHub: https://github.com/tanmay-deev

## 📄 License

MIT License
