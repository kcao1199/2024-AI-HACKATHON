# 2024-AI-HACKATHON
# Team PawsitiveAI

This repository contains the Python scripts and files required to build the "GovQuery Search" - an AI Search solution as part of the 2024 AI Hack-a-thon challenge. The AI Search solution is designed to utilize public data sources to better ingest, process, and provide insightful knowlege management system for federal and state agencies, schools, businesses, and non-profit. 

## Overview

The AI Search solution consists of the following main components:

1. `upload_docs.py`: Python script responsible for uploading dataset and data files from various data sources. This script upload data files in various formats such as CSV, JSON, PPT, PDF, PNG, etc. into an Azure storage account's blob container.
2. `run_indexer.py`
3. `storage.env` and `index.env` are empty environmental files that you need to add your Azure credentials, URI, and API keys to run the Python scripts.
4. `flask_app`:
   * `app.py: Python script that contains Flask app that accepts search queries, performs search with filters, and returns results.
   * template contains html format
5. 
 
## Prerequisites

To run the Python scripts, ensure that you have the following prerequisites set up:

1. Python 3.x installed on your system.
2. Azure CLI configuration (https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-macos)

3. Required Python packages installed. You can install the necessary packages by running the following command in your terminal or command prompt. Be sure to set up an environment as necessary:

* pip install python-dotenv
* pip install azure-identity azure-storage-blob
* pip install azure-search-documents
* pip install flask

## Usage

1. Download and update the environmental files and scripts with the appropriate credentials, file paths, and any other necessary configurations.

2. Run the stages of the AI Search pipeline by executing the following command in your terminal or command prompt within the designated environment:
       python upload_docs.py
       python run_indexer.py
       python app.py
   
   Sequentially execute steps for uploading new datasets and files to Azure storage account (blob, relational database, etc.) then re-run the indexer to process and enrich documents for query in index. 
4. Monitor the console output for any errors or log messages during the execution of the scripts. 
5. [include info about setting-up app.py, html templates, and web interface here]
   
6. 
