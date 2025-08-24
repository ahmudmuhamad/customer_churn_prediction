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
git clone https://github.com/yourusername/customer_churn_prediction.git
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

### 4. Run the Project
- Use the scripts in `src/` or Jupyter notebooks in `notebooks/` for data processing, training, and evaluation.
- Model artifacts and evaluation results are saved in `models/` and `docs/` respectively.

## Documentation & Reports
- Detailed experiment results, error analysis, and prediction outputs are available in the `docs/` folder.
- Visualizations and figures are stored in `reports/figures/`.

## License
This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details.

## Contact
For questions or contributions, please open an issue or submit a pull request.


        
