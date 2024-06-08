from flask import Flask, render_template  # Import the Flask class and the render_template function

# Initialize the Flask application by creating an instance of the Flask class
app = Flask(__name__)

# Define the route for the home page
@app.route('/')  # This decorator associates the URL path '/' with the home function
def home():
    # Render the index.html template from the templates directory and return it as the response
    return render_template('index.html')

# Check if this script is being run directly (not imported as a module)
if __name__ == '__main__':
    # Run the Flask application with debug mode enabled
    app.run(debug=True)  # Debug mode allows for automatic reloading and detailed error messages
