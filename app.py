from flask import Flask, render_template, jsonify
import boto3

app = Flask(__name__)

# Initialize DynamoDB resource
dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')  # Replace with your AWS region
table = dynamodb.Table('WaterQualityData')  # Replace with your DynamoDB table name

# Route to serve the webpage
@app.route('/')
def home():
    return render_template('device.html')  # Make sure your HTML file is named index.html and inside templates/

# API to fetch data from DynamoDB
@app.route('/get_data', methods=['GET'])
def get_data():
    try:
        # Scan the table for data
        response = table.scan()
        items = response.get('Items', [])
        print("Fetched items:", items)  # Debug print
        # Return the data as JSON
        return jsonify(items), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
