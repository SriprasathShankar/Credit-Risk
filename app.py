import streamlit as st
import pandas as pd
import joblib

# 1. FIX: Use raw string (r'') for Windows path and corrected extension to .pkl
# 2. FIX: Using a variable for the model path for cleaner code
MODEL_PATH = r'C:\Users\HP\Python\Projects\ML Project\Credit Risk\random_forest_credit_model.pkl'

try:
    model = joblib.load(MODEL_PATH)
except FileNotFoundError:
    st.error(f"Error loading model: File not found at {MODEL_PATH}")
    st.stop()

# 3. FIX: Corrected dictionary comprehension for encoders
encoder_cols = ['Sex', 'Housing', 'Saving accounts', 'Checking account']
encoders = {}
for col in encoder_cols:
    try:
        # Assuming encoder files are named 'Sex_encoder.pkl', etc.
        encoders[col] = joblib.load(f"{col}_encoder.pkl")
    except FileNotFoundError:
        st.error(f"Error loading encoder: File not found for column '{col}' (expected: {col}_encoder.pkl).")
        st.stop()


st.title('Credit Risk Prediction App')
st.write('Enter Applicant Information to predict if the credit risk is good or bad')

# 4. FIX: Corrected the argument order: min_value=18, max_value=80
age = st.number_input('Age', min_value=18, max_value=80, value=30)
sex = st.selectbox('Sex', ['male', 'female'])
job = st.number_input('Job (0-3)', min_value=0, max_value=3, value=1)
housing = st.selectbox('Housing', ['own', 'rent', 'free'])
saving_accounts = st.selectbox('Saving Accounts', ['little', 'moderate', 'quite rich', 'rich'])
checking_account = st.selectbox('Checking Accounts', ['little', 'moderate', 'rich'])
credit_amount = st.number_input('Credit Amount', min_value=0, value=1000)
duration = st.number_input('Duration (months)', min_value = 1, value=12)

input_df = pd.DataFrame({
    'Age': [age],
    # 5. FIX: Added missing comma after the list
    'Sex': [encoders['Sex'].transform([sex])[0]],
    'Job': [job],
    # 6. FIX: Added missing comma after the list
    'Housing': [encoders['Housing'].transform([housing])[0]],
    # 7. FIX: Added missing comma after the list
    'Saving accounts': [encoders['Saving accounts'].transform([saving_accounts])[0]],
    # 8. FIX: Added missing comma after the list
    'Checking account': [encoders['Checking account'].transform([checking_account])[0]],
    'Credit amount': [credit_amount], # 'credit_account' was used as variable name
    'Duration': [duration]
})

if st.button('Predict credit risk'):
    try:
        pred = model.predict(input_df)
        # 9. FIX: Access the first element of the prediction array
        if pred[0] == 1:
            st.success('The credit score is **Good**') # Use st.success for positive result
        else:
            st.error('The credit score is **Bad**') # Use st.error for negative result
    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")