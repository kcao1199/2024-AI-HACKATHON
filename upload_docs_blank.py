"""1. Navigate to directory in Visual Studio Code
2. Open new terminal. Download Azure CLI in terminal OS/Windows brew update && brew upgrade azure-cli" 
2. Visual Studio Code, download Azure CLI extension
3. Run "az login" in VSC terminal and point to student directory
4. Install Python libraries - 
    pip install python-dotenv
    pip install azure-identity azure-storage-blob
5. Modify storage env file as necessary
6. Input file/folder path below"""


# Import libraries
import os
import logging
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv

# Load environmental variables from file
load_dotenv('storage.env') 

# Read storage account key, storage account name, connection string, and container name from environmental variables
storage_account_key = os.getenv('storage_account_key')
storage_account_name = os.getenv('storage_account_name')
connection_string = os.getenv('connection_string')
container_name = os.getenv('container_name')

# Configuration log
logging.basicConfig(filename='upload_blob.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

# Create the BlobServiceClient object
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# Create a container if it doesn't exist
container_client = blob_service_client.get_container_client(container_name)
try:
    container_client.create_container()
    print(f"Container '{container_name}' created.")
except Exception as e:
    print(f"Container '{container_name}' already exists.")

# Upload the file
def upload_to_blob(file_path, file_name):
    try:        
        # Get a BlobClient object for the specified blob
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_name)
        
        # Upload the file
        with open(file_path, "rb") as data:
            blob_client.upload_blob(data)
        
        print(f"Uploaded {file_name}.")
    except Exception as e:
        print(f"Failed to upload {file_name}: {e}")
    
# Loop through a folder to upload all documents
def upload_folder_to_blob(folder_path):
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        upload_to_blob(file_path, file_name)

# Upload a single file
# upload_to_blob("file_path", "file_name") #Input file name

# Upload all files in a folder
upload_folder_to_blob("folder_path")  #Input folder name



