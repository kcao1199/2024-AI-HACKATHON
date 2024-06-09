import os
from flask import Flask, render_template, request, jsonify, send_file
from dotenv import load_dotenv
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from azure.storage.blob import BlobServiceClient
from io import BytesIO

# Load environment variables from the specified .env file
load_dotenv('index.env')

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

# Define the route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Define the route for the search functionality
@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q')
    
    # Perform the search query
    results = search_client.search(search_text=query)

    # Prepare the response
    response = []
    for result in results:
        blob_name = result['metadata_storage_name'] if 'metadata_storage_name' in result else 'N/A'
        blob_url = f"https://{os.getenv('storage_account_name')}.blob.core.windows.net/{container_name}/{blob_name}"
        
        item = {
            "name": blob_name,
            "sentiment_label": result['sentiment'] if 'sentiment' in result else 'N/A',
            "keyphrases": result['keyphrases'][:5] if 'keyphrases' in result else [],
            "organizations": result['organizations'][:5] if 'organizations' in result else [],
            "locations": result['locations'][:5] if 'locations' in result else [],
            "path": blob_url
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
