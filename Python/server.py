from flask import Flask, request, jsonify
import requests
import os
import json
from dotenv import load_dotenv
from utils.maps import map_place_in_PlacesReview, calculate_average_sentiment
load_dotenv()
from sentiment_analyzers.get_analyzer import get_analyzer

app = Flask(__name__)

GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')
PORT = 3000
sentiment_analyzer = get_analyzer("vader")
sentiment_analyzer.load_model()


@app.route('/searchNearbyRestaurants', methods=['POST'])
def search_nearby_restaurants():
    # Recupera i parametri dal body della richiesta
    data = request.get_json()
    latitude = data.get('latitude', 37.7937)  # valore di default se non fornito
    longitude = data.get('longitude', -122.3965)
    radius = data.get('radius', 500.0)

    try:
        api_url = 'https://places.googleapis.com/v1/places:searchNearby'

        request_body = {
            "includedTypes": ["restaurant"],
            "maxResultCount": 10,
            "locationRestriction": {
                "circle": {
                    "center": {
                        "latitude": latitude,
                        "longitude": longitude
                    },
                    "radius": radius
                }
            }
        }

        headers = {
            'Content-Type': 'application/json',
            'X-Goog-FieldMask': 'places.displayName,places.location,places.rating,places.reviews,places.id'
        }
    
        response = requests.post(
            f"{api_url}?key={GOOGLE_API_KEY}",
            headers=headers,
            json=request_body
        )
        response.raise_for_status()

        review = map_place_in_PlacesReview(response.json())

        score = calculate_average_sentiment(review, sentiment_analyzer)

        print("score", score)

        # Puoi decidere cosa restituire al client
        return jsonify(response.json())

    except requests.exceptions.RequestException as error:
        print('Errore nella chiamata all\'API Places:', str(error))
        return jsonify({'error': 'Errore nel recupero dei ristoranti vicini'}), 500

if __name__ == '__main__':
    app.run(port=PORT, debug=True)