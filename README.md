# 2024-AI-HACKATHON
# Team PawsitiveAI

This repository contains the Python scripts and files required to build the "GovQuery Search" - an AI Search solution as part of the 2024 AI Hack-a-thon challenge. The AI Search solution is designed to utilize public data sources to better ingest, process, and provide insightful knowledge management system for federal and state agencies, schools, businesses, and non-profit. 

## Overview

The AI Search solution consists of the following main components:

1. `upload_docs.py`: Python script responsible for uploading dataset and data files from various data sources. This script upload data files in various formats such as CSV, JSON, PPT, PDF, PNG, etc. into an Azure storage account's blob container.
2. `run_indexer.py`
3. `storage.env` and `index.env` are empty environmental files that you need to add your Azure credentials, URI, and API keys to run the Python scripts.
4. `flask_app`:
   * `app.py`: Python script that contains Flask app that accepts search queries, performs search with filters, and returns results.
   * `/template` directory contains the html format(s)
## Features
![alt text](https://github.com/kcao1199/2024-AI-HACKATHON/blob/main/Architecture.PNG)
* Ingest data from multiple formats: CSV, JSON, PPT, PDF, PNG, etc.
* Perform indexing and enrichment of documents for efficient querying.
* Provide a user-friendly web interface for search queries with filters.

## Prerequisites

To run the Python scripts, ensure that you have the following prerequisites set up:

1. Python 3.x installed on your system. [Download Python](https://www.python.org/downloads/)
2. **Azure CLI** configuration. [Install Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-macos)
3. Required Python packages installed. You can install the necessary packages by running the following command in your terminal or command prompt. Be sure to set up an environment as necessary

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/kcao1199/2024-AI-HACKATHON.git
    cd 2024-AI-HACKATHON
    ```

2. **Install Required Python Packages**:
    ```bash
    pip install python-dotenv azure-identity azure-storage-blob azure-search-documents flask
    ```

## Usage
  
1. **Create and Update Environment Files**:
   - Fill in the provided environmental files with your Azure credentials and configurations.
     
2. Run the stages of the AI Search pipeline by executing the following command in your terminal or command prompt within the designated environment:
    ```bash
       python upload_docs.py
       python run_indexer.py
       python flask_app/app.py
    ```
   
3. Sequentially execute steps for uploading new datasets and files to Azure storage account (blob, relational database, etc.) then re-run the indexer to process and enrich documents for query in index. 
4. Monitor the console output for any errors or log messages during the execution of the scripts. 
5. **Access the Web Interface**:
    Open your web browser and navigate to the URL provided by the Flask server (typically `http://127.0.0.1:5000`) to access the search interface.

### Troubleshooting

If you encounter any issues during setup or usage, refer to the following troubleshooting tips:

1. **Azure CLI Configuration**: Ensure that your Azure CLI is properly configured with the correct subscription and permissions. You can verify this by running `az account show` in your terminal and checking that the correct subscription is active.

2. **Python Environment**: If you encounter errors related to missing packages or compatibility issues, double-check that you are using the correct Python environment. Consider using a virtual environment to isolate dependencies.

3. **Environmental File Configuration**: Check that your `storage.env` and `index.env` files are correctly configured with the required Azure credentials, URI, and API keys. Any typos or incorrect formatting can lead to authentication failures.

4. **File Upload**: If the `upload_docs.py` script fails to upload files to Azure storage, ensure that the file paths are correct and that you have the necessary permissions to access the files.

5. **Indexing Process**: If the `run_indexer.py` script encounters errors during the indexing process, check the console output for specific error messages. Common issues include invalid document formats or connectivity problems with the Azure search service.

6. **Web Interface**: If you are unable to access the web interface served by Flask, ensure that the Flask app is running correctly (`python flask_app/app.py`) and that there are no firewall or network restrictions blocking access to port 5000.

7. **Logging and Debugging**: Enable logging and debugging in your scripts to capture detailed information about any errors or issues encountered. This can help pinpoint the root cause of problems and facilitate troubleshooting.

By following these troubleshooting tips and leveraging community support, you should be able to resolve most issues encountered while setting up or using the AI Search solution.
## Acknowledgements

We extend our gratitude to [Women in Cloud](https://www.womenincloud.com/) and [Microsoft](https://www.microsoft.com) for organizing and hosting this Hackathon AI challenge. Their commitment to fostering diversity and innovation in the tech industry has provided us with a valuable opportunity to showcase our skills and develop impactful solutions. We appreciate their support and dedication to empowering individuals and communities through technology.
