# 2024-AI-HACKATHON
# Team PawsitiveAI

This repository contains the Python scripts and files required to build the AI Search solution as part of the 2024 AI Hack-a-thon challenge. The AI Search solution is designed to utilize public data sources to better ingest, process, and provide insightful knowlege management system for federal and state agencies, schools, businesses, and non-profit. 

## Overview

The AI Search solution consists of the following main components:

1. `upload_docs.py`: Python script responsible for uploading dataset and data files from various data sources. This script upload data files in various formats such as CSV, JSON, PPT, PDF, PNG, etc. into an Azure storage account's blob container.

2. `AI_search.py`: Python script that initializes the Search solution.
 
## Prerequisites

To run the python scripts, ensure that you have the following prerequisites set up:

1. Python 3.x installed on your system.
2. Azure CLI configuration (https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-macos)

3. Required Python packages installed. You can install the necessary packages by running the following command in your terminal or command prompt. Be sure to set-up an environment as necessary:

      pip install python-dotenv
   
      pip install azure-identity azure-storage-blob

## Usage

1. Update the configuration files and scripts with the appropriate credentials, file paths, and any other necessary configurations.

2. Run the stages of the pipeline by executing the following command in your terminal or command prompt:
       python storage2.py
       python transformation2.py
       python transformation_final.py
   
   Sequentially execute steps for extraction and transformation of the datasets. 
4. Monitor the console output for any errors or log messages during the execution of the scripts. 

5. 
   
6. 
