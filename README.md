# 🏡 Plot Price Prediction using Machine Learning

This project predicts land/plot prices based on several property features using machine learning models. A user-friendly interface is provided via a **Streamlit** web app.

---

## 📂 Project Structure

📁 plot_price_prediction/ ├── app1.py ├── index.html ├── 
requirements.txt├──  cleaned_plot_price_prediction_dataset.csv ├── model.pkl └── README.md

---

## 📌 Objective

To build a machine learning pipeline that can predict land plot prices (in Lakhs ₹) based on:

- Location
- Area (in sq. ft.)
- Access to road, water, electricity
- Distance to city (in km)
- Number of nearby schools

---

## 🧰 Technologies Used

- Python
- Pandas, NumPy
- Scikit-learn
- Streamlit
- HTML (for front-end interface)
- Pickle (for model serialization)

---

## 🧼 Data Cleaning

- Dataset: `uncleaned_plot_price_prediction_dataset.csv`
- Columns:

'Location', 'Area_sqft', 'Road_Access', 'Electricity_Access', 'Water_Access', 'Distance_to_City_km', 'Nearby_Schools', 'Price_INR_Lakhs'

- Inspected using `.describe()`, `.info()`, and `.isnull().sum()`
- Missing values handled using:
- Mean for numerical columns
- Mode for categorical columns
- Cleaned dataset saved as `cleaned_plot_price_prediction_dataset.csv`

---

## 🧠 Model Building

### 🎯 Features & Target

- **Independent Variables (X)**: All columns except `Price_INR_Lakhs`
- **Dependent Variable (y)**: `Price_INR_Lakhs`

### 🛠 Preprocessing

- Applied **OneHotEncoding** to categorical columns (like `Location`, `Road_Access`, etc.)
- Used `make_column_transformer` for custom preprocessing steps

### 📦 Pipeline

- Combined encoding and model in a **Pipeline**
- Used train-test split for validation

### 🤖 Models Evaluated

| Model Name              | Full Form                   | Accuracy (%) |
|-------------------------|-----------------------------|--------------|
| `LR`                   | Linear Regression           | 90.64        |
| `RFR`                  | Random Forest Regressor     | 92.89        |
| `DTR`                  | Decision Tree Regressor     | **98.82**    |

✅ **Decision Tree Regressor** performed best and was used for final prediction.

---

## 🧪 Model Deployment

- Final pipeline was saved using `pickle` as `model.pkl`
- `app.py` contains the Streamlit app for taking user input and showing prediction
- `index.html` was used to design a minimal UI interface for integration