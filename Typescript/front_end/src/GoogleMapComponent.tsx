import React, { useState, useCallback } from 'react';
import { GoogleMap, LoadScript, Marker } from '@react-google-maps/api';

interface GoogleMapComponentProps {
  onCoordinateSelect?: (coordinates: { lat: number; lng: number }) => void;
  apiKey: string;
}

const containerStyle = {
  width: '100%',
  height: '400px',
};

const center = {
  lat: 43.7283, // Coordinate di Pisa come centro predefinito
  lng: 10.4039,
};

const GoogleMapComponent: React.FC<GoogleMapComponentProps> = ({ apiKey, onCoordinateSelect }) => {
  const [markerPosition, setMarkerPosition] = useState<{ lat: number; lng: number } | null>(null);

  const onMapClick = useCallback((event: google.maps.MapMouseEvent) => {
    const lat = event.latLng!.lat();
    const lng = event.latLng!.lng();
    setMarkerPosition({ lat, lng });
    if (onCoordinateSelect) {
      onCoordinateSelect({ lat, lng });
    }
  }, [onCoordinateSelect]);

  return (
    <LoadScript googleMapsApiKey={apiKey} libraries={['places']}>
      <GoogleMap
        mapContainerStyle={containerStyle}
        center={center}
        zoom={8}
        onClick={onMapClick}
      >
        {markerPosition && <Marker position={markerPosition} />}
      </GoogleMap>
    </LoadScript>
  );
};

export default GoogleMapComponent;