# Create their own index.env file: You need to create an index.env file in the same directory as the Flask application, containing their Azure-related environment variables (service_endpoint, query_key, service_name, connection_string, container_name).
# Set up Azure services: You need to set up Azure Search and Azure Blob Storage services, and obtain the necessary credentials and endpoint URLs.
# Install Python dependencies: You need to install the required Python dependencies (Flask, python-dotenv, azure-core, azure-search-documents, azure-storage-blob) using pip.
# Run the Flask application: You can then run the Flask application by executing the script, which will start the web server and make the application accessible through a web browser.

import os
from flask import Flask, render_template, request, jsonify, send_file
from dotenv import load_dotenv
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from azure.storage.blob import BlobServiceClient, generate_blob_sas, BlobSasPermissions
from datetime import datetime, timedelta

# Load environment variables from the specified .env file
load_dotenv('index.env')  # Ensure the correct filename is specified

# Initialize the Flask application
app = Flask(__name__)

# Azure Search and Storage configuration
search_endpoint = os.getenv('service_endpoint')
search_key = os.getenv('query_key')
search_index = os.getenv('service_name')
connection_string = os.getenv('connection_string')
container_name = os.getenv('container_name')

# Ensure all necessary environment variables are loaded
if not all([search_endpoint, search_key, search_index, connection_string, container_name]):
    raise ValueError("One or more environment variables are missing.")

# Initialize the Azure Search client
search_client = SearchClient(endpoint=search_endpoint, index_name=search_index, credential=AzureKeyCredential(search_key))

# Initialize the Azure Blob Service client
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# Pre-processing of results
# List of nonsense phrases
unwanted_phrases = [
    "Number Percent",
    "SmartFind Flu ChatBot",
    # Add more unwanted phrases here
]

# Function to filter unwanted keyphrases
def filter_keyphrases(keyphrases):
    # Create a combined regex pattern for all unwanted phrases
    pattern = re.compile(r'\b(?:' + '|'.join(re.escape(phrase) for phrase in unwanted_phrases) + r')\b', re.IGNORECASE)
    
    # Filter out keyphrases that contain any of the unwanted phrases
    return [phrase for phrase in keyphrases if not pattern.search(phrase)]

# Define the route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Define the route for the search functionality
@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q')
    filter_field = request.args.get('filter_field')
    filter_value = request.args.get('filter_value')
    
    # Perform the search query with filters
    # Modify this part to apply your filters to the search query
    results = search_client.search(search_text=query, filter_field=filter_field, filter_value=filter_value)

    # Prepare the response
    response = []
    for result in results:
        item = {
            "name": result['metadata_storage_name'] if 'metadata_storage_name' in result else 'N/A',
            "sentiment_label": result['sentiment'] if 'sentiment' in result else 'N/A',
            "keyphrases": result['keyphrases'][:5] if 'keyphrases' in result else [],
            "organizations": result['organizations'][:5] if 'organizations' in result else [],
            "locations": result['locations'][:5] if 'locations' in result else [],
            "path": result['metadata_storage_path']
        }
        response.append(item)
    
    return jsonify(response)

# Define the route to get a file
@app.route('/get-file', methods=['GET'])
def get_file():
    file_path = request.args.get('path')
    
    # Validate the file path
    if not file_path:
        return jsonify({"error": "File path is required"}), 400
    
    # Extract the blob name from the file path
    blob_name = file_path.split('/')[-1]
    
    # Get the blob client
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
    
    # Download the blob content
    stream = blob_client.download_blob()
    file_content = stream.readall()

    # Return the file as a downloadable response
    return send_file(BytesIO(file_content), as_attachment=True, download_name=blob_name)

# Check if the script is being run directly (not imported as a module)
if __name__ == '__main__':
    app.run(debug=True)
