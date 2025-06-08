# 🟡 Gold Price Prediction Project

## 📌 About

This project aims to predict gold prices using a machine learning model based on various economic indicators. The dataset includes features like **SPX, SLV, EUR/USD**, and **Date**, with the target variable being **GLD (gold price)**. The project covers:

* **Data Cleaning and Preprocessing:** Formatting dates, handling missing values, and feature engineering (e.g., extracting Year and Month).
* **Exploratory Data Analysis (EDA):** Visualizing trends, distributions, and correlations.
* **Model Building:** Training a **Random Forest Regressor** for gold price prediction.
* **Model Evaluation:** Using metrics such as R² Score, MAE, MSE, and RMSE to assess model performance.
* **Streamlit Web App:** An interactive app where users input features (SPX, SLV, Year, Month) to predict gold prices and view trend graphs.
* **Visualization:** Interactive plots showing historical and predicted gold prices.

## 🗂️ Project Structure

```
gold-price-prediction/
│
├── gold_data.csv                # Original dataset
├── gold_data_processed.csv      # Cleaned and preprocessed dataset
├── gold_price_prediction.ipynb  # Jupyter Notebook with data analysis and modeling
├── app.py                       # Streamlit app for interactive predictions
├── requirements.txt             # List of required Python packages
└── README.md                    # Project documentation
```

## 🚀 How to Run

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Tahiruddin1918/Gold-Price-Perdiction.git
   cd Gold-Price-Perdiction
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app:**

   ```bash
   streamlit run app.py
   ```

## 🛠️ Features

✅ Data cleaning and preprocessing
✅ Exploratory data analysis (EDA)
✅ Random Forest Regression model
✅ Model evaluation using multiple metrics
✅ Interactive Streamlit web app with:

* Select boxes for Year and Month
* Graph showing historical and predicted gold prices

## 📊 Model Performance

* **Random Forest Regression:**

  * Training R² Score: 0.999
  * Testing R² Score: 0.996
  * MAE: 0.93
  * MSE: 2.02
  * RMSE: 1.42

* **Linear Regression (baseline):**

  * Training R² Score: 0.91
  * Testing R² Score: 0.89
  * MAE: 5.42
  * MSE: 57.30
  * RMSE: 7.57

## 🔍 Future Improvements

* Hyperparameter tuning for better model performance
* Incorporate more features or external datasets
* Save the trained model using Pickle for deployment
* Add a forecast feature for future months
