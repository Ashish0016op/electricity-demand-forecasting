# Electricity Demand Forecasting

## Introduction
This project focuses on forecasting electricity demand using historical data along with temperature and humidity.  
The goal is to build a predictive model that helps in understanding and forecasting electricity consumption trends.

## Project Type
Data Science | Machine Learning

## Dataset
- `Electricity+Demand+Dataset.csv`
Contains features such as:
- Timestamp
- Hour, Day, Month, Year
- Temperature
- Humidity
- Demand (Target variable)

## Model
I have trained an **XGBoost Regression model** for demand forecasting.  
Final trained model is saved as `electicity_xgb_prediction_model.pkl`.

## Features
- Data Preprocessing & Cleaning
- Exploratory Data Analysis (EDA)
- Feature Engineering (lag, rolling, weather features)
- Machine Learning Model (XGBoost)
- Model Evaluation (MAE, RMSE, R²)

## Installation & Getting Started
Clone the repo and install requirements:

```bash
git clone https://github.com/Ashish0016op/electricity-demand-forecasting.git
cd electricity-demand-forecasting
pip install -r requirements.txt
```
Usage:
- Explore the dataset in the data/ folder.
- Run the notebook for full pipeline (EDA → Feature Engineering → Modeling).
- Load the saved model (.pkl) to make predictions on new data.

Results:
- Model: XGBoost Regressor
- Achieved low error metrics compared to baseline.
- Visualization of demand trends, seasonal patterns, and forecasted demand.

Technology Stack:
- Python
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn
- XGBoost
- Jupyter Notebook
