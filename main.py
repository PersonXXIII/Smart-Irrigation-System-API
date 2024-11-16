from flask import *
import joblib
from datetime import datetime
import os
import csv

# Load the trained model
model = joblib.load('soil_moisture_model.pkl')

# Manually define the class labels list
class_labels = ['Very Dry', 'Dry', 'Wet', 'Very Wet']  # Replace with your actual class names

# Create a Flask app instance
app = Flask(__name__)

# Initialize the data list
data_list = []
# Define the CSV file path
csv_file_path = 'Data/history.csv'
# Variable to store the latest data
latest_data = {}

@app.route('/')
def index():
    return 'Welcome!!'

@app.route('/predict', methods=['POST'])
def predict():
    # Get JSON data from the request
    data = request.get_json()
    
    # Check if all required fields are provided
    if 'temperature' not in data or 'pressure' not in data or 'altitude' not in data or 'soil_moisture' not in data:
        return jsonify({'error': 'Missing input data'}), 400

    # Prepare the input data for the model
    new_data = [[data['temperature'], data['pressure'], data['altitude'], data['soil_moisture']]]

    # Predict the class
    prediction = model.predict(new_data)
    predicted_class_name = class_labels[prediction[0]]
    
    timestamp = datetime.now().strftime('%H:%M:%S')
    date = datetime.now().strftime('%Y-%m-%d')
    
    # Prepare the data to be saved
    updated_data = {
        'temperature': data['temperature'],
        'pressure': data['pressure'],
        'altitude': data['altitude'],
        'soil_moisture': data['soil_moisture'],
        'predicted_class': predicted_class_name,
        'time': timestamp,
        'date': date
    }
    
    # Store the latest data
    latest_data.update(updated_data)
    # Append the updated data to the list
    data_list.append(updated_data)

    # Save the data to the CSV file
    write_to_csv(updated_data)
    
    # Return the result as a JSON response
    return jsonify({'predicted_class': predicted_class_name})

@app.route('/get_latest_data')
def get_latest_data():
    # Return the latest data as a JSON response
    return jsonify(latest_data)

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")
    
    
def write_to_csv(data):
    # Check if the file exists, if not, create it with headers
    file_exists = os.path.exists(csv_file_path)
    
    with open(csv_file_path, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=data.keys())

        # If the file doesn't exist, write the header
        if not file_exists:
            writer.writeheader()

        # Write the received data as a new row
        writer.writerow(data)

if __name__ == '__main__':
    app.run(debug=True)
