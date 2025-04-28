
const API_BASE = 'http://localhost:3000/';

export const Sentiment_service = {
    async searchNearbyRestaurants(latitude: number, longitude: number, radius: number, activity_type: string): Promise<any> {
        const queryParams = new URLSearchParams({
            latitude: latitude.toString(),
            longitude: longitude.toString(),
            radius: radius.toString(),
            activity_type: activity_type,
        });
        
        const response = await fetch(`${API_BASE}searchNearbyRestaurants?${queryParams}`, {
            method: 'GET'
        });
        
        if (!response.ok) throw new Error('Error searching nearby restaurants');
        return response.json();
    },
};


