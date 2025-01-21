from flask import Flask, jsonify
import requests

app = Flask(__name__)

# Base URL voor Customer.io API (EU-regio, verander dit indien je in de US-regio zit)
CUSTOMER_IO_BASE_URL = "https://api-eu.customer.io/v1/api"

# API Key direct in de code (voor development-doeleinden, niet aanbevolen voor productie)
API_KEY = "7991f3c67ee8b605e81ab35bba06d7a3"

@app.route('/get-campaigns', methods=['GET'])
def get_campaigns():
    # URL voor het ophalen van campagnes
    url = f"{CUSTOMER_IO_BASE_URL}/campaigns"
    
    # Headers voor authenticatie
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    # Verzoek versturen
    response = requests.get(url, headers=headers)
    
    # Foutafhandeling
    if response.status_code != 200:
        return jsonify({
            "error": "Kan campagnes niet ophalen",
            "status_code": response.status_code,
            "details": response.text
        }), response.status_code
    
    # Data teruggeven
    return jsonify(response.json())

if __name__ == "__main__":
    # Laat de server luisteren op alle netwerkinterfaces en gebruik de juiste poort
    app.run(host="0.0.0.0", port=5000)
