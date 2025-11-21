Ranelagh Time Keeping

A prototype barcode-based race timing system, inspired by parkrun.
This project demonstrates an event-driven, serverless workflow using AWS services to ingest race results, match athletes to barcodes, store them, and display them via a simple web interface.

Overview

The system takes a results.csv file containing barcode, time, and finish position data.
When uploaded to S3, it triggers a Lambda function that:

Parses the results

Looks up athlete information in DynamoDB

Stores processed data for querying in Athena

Exposes the results to a browser-based front end via API Gateway

A lightweight, static web app (served with CloudFront) allows users to view event results.

This project is a test deployment to explore how such a timing system could be implemented end-to-end using AWS.

Architecture

AWS services used:

S3 – Stores uploaded result files

Lambda – Processes CSV data and enriches it with athlete info

DynamoDB – Maps barcodes to registered runners

Athena – Provides queryable race results

API Gateway – API interface for the front end

CloudFront – Serves the static web app

Web Front End – Simple HTML/JS interface to display results

See the architecture diagram in diagrams/architecture.PNG.

Features

Barcode → user lookup

Automated processing of uploaded race results

Queryable results via Athena

Web page displaying results

Fully serverless, event-driven workflow

Easily extendable for real events

Getting Started
Prerequisites

AWS account with permissions for S3, Lambda, DynamoDB, Athena, API Gateway

Local AWS CLI (optional but helpful)

Node.js (if modifying the front-end code)

Setup & Deployment

Clone the repository

git clone https://github.com/alexr1210/ranelagh-time-keeping.git
cd ranelagh-time-keeping


Create AWS resources

S3 bucket for uploading results

DynamoDB table (e.g., Athletes) with barcode as the primary key

IAM roles for Lambda, Athena access, and S3 triggers

API Gateway endpoint for the front-end app

CloudFront distribution to host the static site

Deploy the Lambda

Package and upload the Lambda function, then configure S3 → Lambda event notifications.

Configure Athena

Create a database and table for results

Ensure output locations are configured correctly in S3

Deploy the front end

Upload the contents of web-front-end/ to your hosting setup (e.g., S3 + CloudFront).

Usage Workflow

Upload a results.csv file to your configured S3 bucket.

The Lambda function processes the file and loads the results into Athena.

The web app fetches processed results via API Gateway.

Runners can view the results in a browser.

Project Structure
├── athletes/           # Data/code related to athlete barcode lookup  
├── diagrams/           # Architecture diagram  
├── results/            # Example CSVs or processed data  
├── templates/          # HTML/JS templates  
├── web-front-end/      # Public-facing website  
└── README.md

Contributing

Contributions are welcome!

Possible enhancements:

Improved front-end UI/UX

Enhanced athlete profiles

Multi-event support

Automated IaC deployment (Terraform/CFT/CDK)

Test suite for the Lambda function

Historical statistics & visualisations

To contribute:

Fork the repo

Create a feature branch

Submit a pull request

Roadmap

Authentication for uploading results

Mobile-friendly front end

Real-time result streaming

Extended stats (PBs, historical rankings)

Multiple events / courses

License

Add a license here (e.g., MIT, Apache 2.0).

Contact

Author: alexr1210
GitHub: https://github.com/alexr1210

Issues & feature requests: GitHub Issues tab
