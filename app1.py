import streamlit as st
import pandas as pd
import pickle

# Load model pipeline
with open('model.pkl', 'rb') as f:
    pipeDTR = pickle.load(f)

st.title("🏡Plot Price Prediction App")

st.write("Fill the details below to estimate a good buying price for a plot.")

# Input fields
Location= st.selectbox("Location📍", ["Rural", "Urban", "Suburban"])
Area_sqft = st.text_input(" Area_sqft🗾(eg. 3234, 3345..etc) ")
Road_Access= st.selectbox("Road_Access 🛣 ", ["Street", "Highway ", "Main Road"])
Electricity_Access = st.selectbox("Electricity_Access💡(Yes=1, No=0)", options=[0, 1])
Water_Access = st.selectbox("Water_Access💧(Yes=1, No=0)", options=[0, 1])
Distance_to_City_km = st.text_input("Distance_to_City_km 🏙 (eg. 32,45..etc)")
Nearby_Schools= st.text_input("Nearby_Schools🏫(eg. 2,3,4..etc)")
# Predict button
if st.button("Predict Price"):
    # Prepare input
    columns=["Location","Area_sqft","Road_Access","Electricity_Access","Water_Access","Distance_to_City_km","Nearby_Schools"]
    myinput=pd.DataFrame(columns=columns,data=[[Location,Area_sqft,Road_Access,Electricity_Access,Water_Access,Distance_to_City_km,Nearby_Schools]])
    
    # Prediction
    try:
        result = pipeDTR.predict(myinput)
        st.success(f"You should buy it for ~ ₹ {abs(round(result[0]))} lakhs")
    except Exception as e:
        st.error(f"Prediction failed: {e}")