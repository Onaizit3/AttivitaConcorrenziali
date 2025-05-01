# Competitiveness Activity Score System

# Competitiveness Activity Score System

## Overview
This program helps you find competitiveness scores for various activities in your area. It analyzes and evaluates the level of competition among businesses and services in a specified location.

**Score Interpretation:**  
The higher the score, the more competition there is in the area.

## Setup Instructions

### API Keys
- You need a Google API key to use this application.
- The following Google Maps Platform APIs must be **enabled** on your key:
  - **Places API (New)**
  - **Maps JavaScript API**
- Insert your API key in both `.env` files (backend and frontend).

#### Obtaining and Restricting Your API Key
1. Go to the Google Cloud Console:  
   https://console.cloud.google.com  
2. Select an existing project or click **Create Project** to make a new one.  
3. In the left-hand menu, navigate to **APIs & Services > Library**.  
4. Search for **Places API (new)** and **Maps JavaScript API**, then click **Enable** on each tile.
5. Go to **APIs & Services > Credentials**, then click **Create credentials > API key**. Copy the key shown.

### Backend (Python)
1. Create a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    ```
2. Install required libraries:
    ```bash
    pip install -r requirements.txt
    ```

### Frontend (TypeScript)
1. Install dependencies:
    ```bash
    npm install
    ```

## Running the Project
1. **Start the backend server**  
    ```bash
    python3 server.py
    ```
2. **Start the frontend development server**  
    ```bash
    npm run dev
    ```

## Usage
After completing the setup, you can run the application to analyze the competitiveness of activities in your chosen area. The system will provide scores based on Google's location data and other metrics.

## Note
Make sure to keep your API key secure and never commit it to version control.  