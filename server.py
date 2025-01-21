from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# API Key en base URL
API_KEY = '7991f3c67ee8b605e81ab35bba06d7a3'  # Vervang dit met jouw API Key
BASE_URL = 'https://api-eu.customer.io/v1'

# Endpoint om campagnes op te halen
@app.route('/get-campaigns', methods=['GET'])
def get_campaigns():
    try:
        response = requests.get(f'{BASE_URL}/api/campaigns', headers={
            'Authorization': f'Bearer {API_KEY}'
        })
        return jsonify(response.json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000)
