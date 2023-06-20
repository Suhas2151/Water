import streamlit as st
import pickle

# Set Streamlit title and page configuration
st.set_page_config(
    page_title="Water Potability Prediction",
    page_icon=":droplet:",
    layout="wide"
)

# Set background image
st.markdown(
    """
    <style>
    .reportview-container {
        background: url('https://hse.ok.ubc.ca/wp-content/uploads/sites/72/2022/10/Water.png') no-repeat center center fixed;
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Load the trained model
model = pickle.load(open("Random_Forest_Water.py", "rb"))  # Replace "your_model.pkl" with the actual file path of your model

# User input for prediction
st.sidebar.title("Enter Water Parameters")
ph = st.sidebar.number_input("pH")
hardness = st.sidebar.number_input("Hardness")
solids = st.sidebar.number_input("Solids")
chloramines = st.sidebar.number_input("Chloramines")
sulfate = st.sidebar.number_input("Sulfate")
conductivity = st.sidebar.number_input("Conductivity")
organic_carbon = st.sidebar.number_input("Organic Carbon")
trihalomethanes = st.sidebar.number_input("Trihalomethanes")
turbidity = st.sidebar.number_input("Turbidity")

# Create feature vector from user inputs
features = [[ph, hardness, solids, chloramines, sulfate, conductivity, organic_carbon, trihalomethanes, turbidity]]

if st.sidebar.button("Predict"):
    # Predict water potability
    prediction = model.predict(features)
    # Display the prediction
    st.subheader("Water Potability Prediction")
     if prediction == 0:
        st.write("Non-Potable Water")
     else:
        st.write("Potable Water")

# Add disclaimer
st.sidebar.markdown("---")
st.sidebar.markdown("**Disclaimer:** This is a simple prediction model and the results may not be accurate. Please consult a water quality expert for precise analysis.")

