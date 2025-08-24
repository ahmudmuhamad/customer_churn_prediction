# Customer Churn Prediction

## Problem Statement
Customer churn is a critical issue for businesses, as retaining existing customers is often more cost-effective than acquiring new ones. This project aims to predict customer churn using machine learning techniques, enabling proactive retention strategies and improved business outcomes.

## Solution Overview
This repository provides a full pipeline for predicting customer churn:
- Data preprocessing and exploratory analysis
- Feature engineering
- Model training and evaluation
- Final model selection and calibration
- Generation of predictions and performance reports

## Final Model
The final model is trained using state-of-the-art algorithms, including XGBoost, Random Forest, and Logistic Regression. The best-performing model is selected based on cross-validation and test metrics, and calibration is applied for probability accuracy. Model artifacts are stored in the `models/` directory.

## Project Structure
```
├── data/                       # Raw and processed data files
├── docker/                     # Dockerfile for containerization
├── docs/                       # Documentation, evaluation, errors, predictions
├── models/                     # Saved model files (.joblib)
├── notebooks/                  # Jupyter notebooks for EDA and experimentation
├── src/                        # Source code
│   ├── churn/                  # Churn prediction modules
│   ├── create.py               # Main script for model creation
├── environment.yml             # Conda environment specification
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation

```

## Getting Started
### 1. Clone the Repository
```bash
git clone https://github.com/ahmudmuhamad/customer_churn_prediction.git
cd customer_churn_prediction
```

### 2. Create and Activate Conda Environment
```bash
conda env create -f environment.yml
conda activate customer_churn_prediction
```

### 3. Install Required Python Modules
If you prefer using pip:
```bash
pip install -r requirements.txt
```

### 4. Run the Server
To start the FastAPI server for serving predictions:
```bash
uvicorn churn.api.main:app --app-dir src --reload --host 0.0.0.0 --port 8000
```

## API Endpoints

- **POST /predict/**  
  Request: JSON with features (single dict or list of dicts) and optional threshold  
  Response: Predictions and probabilities
- **GET /health**  
  Returns: `{ "status": "ok" }` (basic health check)
- **GET /ready**  
  Returns: `{ "ready": true/false }` (model readiness status)

### Example: Using the Predict Endpoint
Send a POST request to `/predict/` with the following JSON body:
```json
{
  "data": {
    "total_events": 100,
    "n_sessions": 10,
    "unique_songs": 20,
    "unique_artists": 5,
    "total_length": 3000,
    "avg_length": 200,
    "avg_itemInSession": 2,
    "num_cancellation_events": 0,
    "num_thumbup": 5,
    "num_thumbdown": 1,
    "num_home": 10,
    "num_nextsong": 50,
    "activity_span_seconds": 86400,
    "last_level": 2,
    "last_location": 1
  },
  "threshold": 0.5
}
```
Example using `curl`:
```bash
curl -X POST "http://localhost:8000/predict/" \
     -H "Content-Type: application/json" \
     -d '{
           "data": {
             "total_events": 100,
             "n_sessions": 10,
             "unique_songs": 20,
             "unique_artists": 5,
             "total_length": 3000,
             "avg_length": 200,
             "avg_itemInSession": 2,
             "num_cancellation_events": 0,
             "num_thumbup": 5,
             "num_thumbdown": 1,
             "num_home": 10,
             "num_nextsong": 50,
             "activity_span_seconds": 86400,
             "last_level": 2,
             "last_location": 1
           },
           "threshold": 0.5
         }'
```
Response:
```json
{
  "predictions": [0],
  "probabilities": [0.23]
}
```

## Documentation & Reports
- Detailed experiment results, error analysis, and prediction outputs are available in the `docs/` folder.
- Visualizations and figures are stored in `reports/figures/`.

## License
This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details.

## Contact
For questions or contributions, please open an issue or submit a pull request.
```


        
