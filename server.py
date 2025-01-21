from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/get-campaigns', methods=['GET'])
def get_campaigns():
    # Dummy data; vervang dit met je eigen logica om data op te halen
    campaigns = [
        {"id": 1, "name": "Campaign 1", "status": "active"},
        {"id": 2, "name": "Campaign 2", "status": "inactive"}
    ]
    return jsonify({"campaigns": campaigns})

if __name__ == "__main__":
    # Laat de server luisteren op alle netwerkinterfaces en gebruik de juiste poort
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
