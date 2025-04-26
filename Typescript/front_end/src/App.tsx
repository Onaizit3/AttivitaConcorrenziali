import React, { useState } from 'react';
import GoogleMapComponent from './GoogleMapComponent';
import {   Button,   Form,   Select, InputNumber, Card, Row, Col,
} from 'antd';
import {smallActivities} from './constants';
import { Sentiment_service } from './services/sentiment_service';

const { Option } = Select;

const App: React.FC = () => {
  const [selectedCoordinates, setSelectedCoordinates] = useState<{ lat: number; lng: number } | null>(null);
  const [range, setRange] = useState<number>(1000); // Default 1000 metri
  const [selectedActivity, setSelectedActivity] = useState<string>('');
  const googleApiKey = import.meta.env.VITE_GOOGLE_API_KEY;

  const handleCoordinateSelect = (coordinates: { lat: number; lng: number }) => {
    console.log('Coordinate selezionate:', coordinates);
    setSelectedCoordinates(coordinates);
  };

  const handleCoordinateChange = (field: 'lat' | 'lng', value: number | null) => {
    if (value === null) return;
    
    setSelectedCoordinates(prev => {
      if (!prev) return { lat: field === 'lat' ? value : 0, lng: field === 'lng' ? value : 0 };
      return { ...prev, [field]: value };
    });
  };

  const handleRangeChange = (value: number | null) => {
    setRange(value || 1000);
  };

  const handleActivityChange = (value: string) => {
    setSelectedActivity(value);
  };

  const handleGetScore = () => {
    Sentiment_service.searchNearbyRestaurants(
      selectedCoordinates?.lat || 0,
      selectedCoordinates?.lng || 0,
      range,
      selectedActivity
    )
    .then((response) => {
      console.log('Risposta dal server:', response);
      // Gestisci la risposta qui
    }
    )
    .catch((error) => {
      console.error('Errore durante la richiesta:', error);
      // Gestisci l'errore qui
    }
    );
  };

  return (
    <div style={{ width: '100vw', height: '100vh', overflow: 'hidden' }}>
      <Row style={{ height: '100%' }}>
        {/* Small space on the left */}
        <Col span={1} />
        
        {/* Map component */}
        <Col span={15} style={{ height: '100vh', display: 'flex', alignItems: 'center' }}>

          <GoogleMapComponent 
            apiKey={googleApiKey} 
            onCoordinateSelect={handleCoordinateSelect} 
          />
        </Col>
        
        {/* Small space in the middle */}
        <Col span={1} />
        
        {/* Form component */}
        <Col span={6} style={{ height: '100vh', display: 'flex', alignItems: 'center' }}>
          <Card style={{ width: '100%' }}>
            <Form layout="vertical">
              <Form.Item label="Latitude">
                <InputNumber
                  value={selectedCoordinates?.lat}
                  onChange={(value) => handleCoordinateChange('lat', value)}
                  style={{ width: '100%' }}
                  min={-90}
                  max={90}
                  precision={6}
                  placeholder="Inserisci la latitudine (-90 a 90)"
                />
              </Form.Item>
              
              <Form.Item label="Longitude">
                <InputNumber
                  value={selectedCoordinates?.lng}
                  onChange={(value) => handleCoordinateChange('lng', value)}
                  style={{ width: '100%' }}
                  min={-180}
                  max={180}
                  precision={6}
                  placeholder="Inserisci la longitudine (-180 a 180)"
                />
              </Form.Item>
              
              <Form.Item label="Range in metri">
                <InputNumber
                  value={range}
                  onChange={handleRangeChange}
                  style={{ width: '100%' }}
                  min={1}
                  max={50000}
                  placeholder="Inserisci il raggio in metri"
                />
              </Form.Item>
              
              <Form.Item label="Attività">
                <Select
                  value={selectedActivity}
                  onChange={handleActivityChange}
                  style={{ width: '100%' }}
                  placeholder="Seleziona un'attività"
                >
                  {smallActivities.map((activity) => (
                    <Option key={activity} value={activity}>
                      {activity}
                    </Option>
                  ))}
                </Select>
              </Form.Item>
              
              <Button 
                type="primary" 
                onClick={handleGetScore}
                style={{ width: '100%' }}
              >
                Get Score
              </Button>
            </Form>
          </Card>
        </Col>
        
        {/* Small space on the right */}
        <Col span={1} />
      </Row>
    </div>
  );
};

export default App;
