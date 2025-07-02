# Getting Started 
You can run this prototype in two ways. Docker is the quickest and recommended method.
## Run with Docker
Make sure you have Docker installed and running on your machine.
### 1. Build the Docker Image
Open your terminal in the project's root directory and run the following command:
```bash
docker build -t OmneNEST_WP_Prototype .
```
### 2. Run the Docker Container
Next, run the container you just built:
```bash
docker run -p 8000:8000 OmneNEST_WP_Prototype
```
The API is now live and accessible at http://localhost:8000.

## Run Locally with Python
### 1. Clone this repository (if you haven't already)
```bash
git clone https://github.com/sidrocks123/OmneNEST_WP_ProtoType.git
cd OmneNEST_WP_Prototype
```
### 2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Run the API Server
```bash
uvicorn app.main:app --reload
```
The API is now live and accessible at http://127.0.0.1:8000.

## How to Test the API
You can use curl or any API client to send requests to the /predict endpoint.
### Test Case 1: A Normal Latency Value
```bash
curl -X 'POST' \
  'http://localhost:8000/predict' \
  -H 'Content-Type: application/json' \
  -d '{
    "latency_ms": 55
  }'
```
#### Expected Response:
```json
{
  "latency_ms": 55,
  "is_anomaly": false,
  "assessment": "Normal"
}
```
### Test Case 2: An Anomalous Latency Value
```bash
curl -X 'POST' \
  'http://localhost:8000/predict' \
  -H 'Content-Type: application/json' \
  -d '{
    "latency_ms": 250
  }'
```
#### Expected Response:
```json
{
  "latency_ms": 250,
  "is_anomaly": true,
  "assessment": "Anomaly Detected"
}
```