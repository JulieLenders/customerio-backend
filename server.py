from flask import Flask, jsonify, request
import os
import requests

app = Flask(__name__)

# Basisconfiguratie
CUSTOMERIO_API_KEY = os.environ.get("CUSTOMERIO_API_KEY")
CUSTOMERIO_BASE_URL = "https://api.customer.io/v1/api"

headers = {
    "Authorization": f"Bearer {CUSTOMERIO_API_KEY}",
    "Content-Type": "application/json"
}

# Functie om data van Customer.io op te halen
def fetch_data(endpoint):
    url = f"{CUSTOMERIO_BASE_URL}{endpoint}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

# Routes
@app.route('/get-campaigns', methods=['GET'])
def get_campaigns():
    data = fetch_data("/campaigns")
    return jsonify(data or {"error": "Unable to fetch campaigns"})

@app.route('/get-segments', methods=['GET'])
def get_segments():
    data = fetch_data("/segments")
    return jsonify(data or {"error": "Unable to fetch segments"})

@app.route('/get-people', methods=['GET'])
def get_people():
    data = fetch_data("/customers")
    return jsonify(data or {"error": "Unable to fetch people"})

@app.route('/get-activity/<customer_id>', methods=['GET'])
def get_activity(customer_id):
    data = fetch_data(f"/customers/{customer_id}/activities")
    return jsonify(data or {"error": f"Unable to fetch activity for customer {customer_id}"})

@app.route('/webhooks', methods=['POST'])
def receive_webhooks():
    webhook_data = request.json
    print("Webhook ontvangen:", webhook_data)
    return jsonify({"message": "Webhook succesvol verwerkt"}), 200

# Start de server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
