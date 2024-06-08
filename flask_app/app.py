import os
from flask import Flask, render_template  # Import the Flask class and the render_template function
from dotenv import load_dotenv

#pip install azure-search-documents 
#pip install python-dotenv
#pip install azure-identity azure-storage-blob
#pip install flask azure-search-documents azure-storage-blob

from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from azure.storage.blob import BlobServiceClient, generate_blob_sas, BlobSasPermissions
from datetime import datetime, timedelta

# Initialize the Flask application by creating an instance of the Flask class
app = Flask(__name__)

# Azure Search constants
load_dotenv(index.env)
search_endpoint = os.getenv('service_endpoint')
search_key = os.getenv('query_key')
search_index = os.getenv('service_name')
connection_string = os.getenv('connection_string')
container_name = os.getenv('container_name')

# Initialize 
search_client = SearchClient(endpoint=search_service_endpoint, index_name=search_index_name, credential=AzureKeyCredential(search_api_key))

# Define the route for the home page
@app.route('/')  # This decorator associates the URL path '/' with the home function
def home():
    # Render the index.html template from the templates directory and return it as the response
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q')
    
    # Perform the search
    results = search_client.search(search_text=query)

    # Prepare the response
    response = []
    for result in results:
        item = {
            "name": result['metadata_storage_name'],
            "path": result['metadata_storage_path']
        }
        response.append(item)
    
    return jsonify(response)

"""@app.route('/get-file-url', methods=['GET'])
def get_file_url():
    file_path = request.args.get('path')
    
    # Extract container and blob name from the file path
    container_client = blob_service_client.get_container_client(container_name)
    
    # Generate a SAS token for secure access
    sas_token = generate_blob_sas(
        account_name=blob_service_client.account_name,
        container_name=container_name,
        blob_name=file_path,
        account_key=blob_service_client.credential.account_key,
        permission=BlobSasPermissions(read=True),
        expiry=datetime.utcnow() + timedelta(hours=1)
    )
    
    blob_url = f"https://{blob_service_client.account_name}.blob.core.windows.net/{container_name}/{file_path}?{sas_token}"
    
    return jsonify({"url": blob_url})"""

# Check if this script is being run directly (not imported as a module)
if __name__ == '__main__':
    # Run the Flask application with debug mode enabled
    app.run(debug=True)  # Debug mode allows for automatic reloading and detailed error messages
