# AI-Driven Sales & Marketing Intelligence Dashboard

## Overview
This project is a Flask-based web application designed to analyze sales data and generate AI-driven insights for sales recommendations, strategies, and marketing funnels. The system leverages Google’s Gemini AI model to process CSV files, extract key insights, and provide actionable business intelligence.

## Features
- Upload and analyze sales data (CSV files)
- Generate AI-powered sales recommendations
- Provide data-driven sales strategies
- Develop targeted marketing funnels
- Interactive web dashboard for seamless user experience

## Technologies Used
- **Backend:** Flask, Flask-CORS
- **AI Integration:** Google Gemini AI
- **Frontend:** HTML, CSS, JavaScript
- **Data Processing:** Pandas
- **Environment Management:** dotenv
- **Logging:** Python Logging Module

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/your-repository.git
   cd your-repository
   ```
2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate   # On macOS/Linux
   venv\Scripts\activate      # On Windows
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Set up environment variables:
   - Create a `.env` file in the project root.
   - Add the following line:
     ```sh
     GEMINI_API_KEY=your_api_key_here
     ```

## Running the Application

1. Start the Flask server:
   ```sh
   python app.py
   ```
2. Open a web browser and navigate to:
   ```sh
   https://captianjack.tech/
   ```

## API Endpoints

### 1. Upload Sales Data
- **Endpoint:** `POST /api/upload-csv`
- **Description:** Uploads and processes a CSV file.
- **Request:** `multipart/form-data`
- **Response:** JSON with analyzed data insights.
- **Usage:**
  ```sh
  curl -X POST -F "file=@sales_data.csv" https://captianjack.tech/api/upload-csv
  ```

### 2. Generate Sales Recommendations
- **Endpoint:** `POST /api/sales-recommendations`
- **Description:** Provides 10 data-driven recommendations to optimize sales.
- **Request:** JSON with analyzed sales data.
- **Response:** JSON with AI-generated recommendations.
- **Usage:**
  ```sh
  curl -X POST -H "Content-Type: application/json" -d '{"analysis": {}}' https://captianjack.tech/api/sales-recommendations
  ```

### 3. Generate Sales Strategies
- **Endpoint:** `POST /api/sales-strategies`
- **Description:** Generates 3 actionable sales strategies.
- **Request:** JSON with analyzed sales data.
- **Response:** JSON with AI-generated strategies.
- **Usage:**
  ```sh
  curl -X POST -H "Content-Type: application/json" -d '{"analysis": {}}' https://captianjack.tech/api/sales-strategies
  ```

### 4. Generate Marketing Funnels
- **Endpoint:** `POST /api/marketing-funnels`
- **Description:** Creates 5 targeted marketing funnels.
- **Request:** JSON with analyzed sales data.
- **Response:** JSON with AI-generated marketing funnels.
- **Usage:**
  ```sh
  curl -X POST -H "Content-Type: application/json" -d '{"analysis": {}}' https://captianjack.tech/api/marketing-funnels
  ```

## Deployment
This application is deployed at: [https://captianjack.tech/](https://captianjack.tech/)

### Deployment Options
- **Docker:** Containerize the application for scalable deployment.
- **Heroku:** Deploy with minimal configuration.
- **AWS Lambda:** Serverless deployment for cost-effective scaling.

## Contributing
1. Fork the repository.
2. Create a new branch (`feature-branch`).
3. Commit your changes.
4. Push the branch and create a Pull Request.

