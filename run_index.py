#Ensure environment has pip install azure-search-documents 

# Import libraries
import os
import sys
import requests
from azure.core.credentials import AzureKeyCredential
from azure.search.documents.indexes import SearchIndexClient, SearchIndexerClient
from dotenv import load_dotenv


# Load env file
load_dotenv('index.env') 

# Read for info
service_endpoint = os.getenv('service_endpoint')
key = os.getenv('query_key')
indexer_name = os.getenv('indexer_name')

#Initializa Indexer 
indexer_client = SearchIndexerClient(service_endpoint, AzureKeyCredential(key))


def run_indexer(indexer_name):
    try:
        result = indexer_client.run_indexer(indexer_name)
        print(f"Ran the Indexer '{indexer_name}'")
        return result
    except Exception as e:
        print(f"Error running indexer: {e}")

def reset_indexer(indexer_name):
    try:
        result = indexer_client.reset_indexer(indexer_name)
        print(f"Reset the Indexer '{indexer_name}'")
        return result
    except Exception as e:
        print(f"Error resetting indexer: {e}")

"""def delete_indexer(indexer_name):
    try:
        indexer_client.delete_indexer(indexer_name)
        print(f"Indexer '{indexer_name}' successfully deleted")
    except Exception as e:
        print(f"Error deleting indexer: {e}")"""


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py [run|reset]")
        sys.exit(1)

    action = sys.argv[1]
    if action == "run":
        run_indexer(indexer_name)
    elif action == "reset":
        reset_indexer(indexer_name)
    #elif action == "delete"
         #delete_indexer(indexer_name)
    else:
        print("Invalid action. Please choose from 'run' or 'reset'.")
        sys.exit(1)