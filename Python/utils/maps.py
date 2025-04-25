
from classes.places_review import PlacesReview
from typing import List, Optional
from sentiment_analyzers.sentiment_analyzer import SentimentAnalyzer

def map_place_in_PlacesReview(data):
    result = []
    for place in data.get('places', []):
        place_info = PlacesReview()
        # Prende il rating del posto (se presente)
        place_info.rating = place.get('rating', None)
        # Estrae tutti gli originalText dalle recensioni
        reviews_texts = []
        for review in place.get('reviews', []):
            if 'originalText' in review and 'text' in review['originalText']:
                reviews_texts.append(review['originalText']['text'])
        place_info.reviews = reviews_texts
        result.append(place_info)
    return result

def calculate_average_sentiment(places_reviews, sentiment_analyzer: SentimentAnalyzer) -> Optional[float]:
    place_averages = []
    
    for place_review in places_reviews:
        if not place_review.reviews:
            continue
            
        sentiments = [sentiment_analyzer.analyze(review) for review in place_review.reviews]
        if sentiments:
            place_averages.append(sum(sentiments) / len(sentiments))
    
    return sum(place_averages) / len(place_averages) if place_averages else None