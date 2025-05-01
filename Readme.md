# Competitiveness Activity Score System

## Overview
This program helps you find competitiveness scores for various activities in your area. It analyzes and evaluates the level of competition among businesses and services in a specified location.

Currently, the algorithm simply calculates the average sentiment analysis of nearby activities to determine competitiveness scores.

## Setup Instructions

### API Keys
- You need a Google API key to use this application
- Insert your API key in both .env files (backend and frontend)

### Backend (Python)
1. Create a virtual environment:
    ```
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    ```
2. Install required libraries:
    ```
    pip install -r requirements.txt
    ```

### Frontend (TypeScript)
1. Install dependencies:
    ```
    npm install
    ```

## Usage
After completing the setup, you can run the application to analyze the competitiveness of activities in your chosen area. The system will provide scores based on Google's location data and other metrics.

## Note
Make sure to keep your API key secure and never commit it to version control.