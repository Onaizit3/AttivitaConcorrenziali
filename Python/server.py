from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os
import json
from dotenv import load_dotenv
from utils.maps import map_place_in_PlacesReview, calculate_average_sentiment
load_dotenv()
from sentiment_analyzers.get_analyzer import get_analyzer

app = Flask(__name__)
CORS(app) #:TODO remove if it should go to production

GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')
PORT = 3000
sentiment_analyzer = get_analyzer("vader")
sentiment_analyzer.load_model()


@app.route('/searchNearbyRestaurants', methods=['GET'])
def search_nearby_restaurants():

    latitude = request.args.get('latitude', default=37.7937, type=float)
    longitude = request.args.get('longitude', default=-122.3965, type=float)
    radius = request.args.get('radius', default=500.0, type=float)
    activity_type = request.args.get('activity_type', default='restaurant', type=str)

    try:
        api_url = 'https://places.googleapis.com/v1/places:searchNearby'

        request_body = {
            "includedTypes": [activity_type],
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

        return jsonify("The score is: " + str(score)), 200

    except requests.exceptions.RequestException as error:
        print('Error in the Places API call:', str(error))
        return jsonify({'error': 'Error retrieving nearby restaurants'}), 500

if __name__ == '__main__':
    app.run(port=PORT, debug=False)

