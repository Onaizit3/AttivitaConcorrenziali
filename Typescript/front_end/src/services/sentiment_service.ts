
const API_BASE = 'http://localhost:3000/';

export const Sentiment_service = {

async searchNearbyRestaurants(latitude: number, longitude: number, radius: number, type: string ): Promise<any> {
    const response = await fetch(`${API_BASE}searchNearbyRestaurants`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            latitude,
            longitude,
            radius,
            type
        })
    });
    
    if (!response.ok) throw new Error('Error searching nearby restaurants');
    return response.json();
},
};


