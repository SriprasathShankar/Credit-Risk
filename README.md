**📈 Credit Risk Classification & Deployment Project**


**✨ 1. Overview**

This project is an end-to-end Machine Learning solution designed to classify the credit risk of loan applicants as either Good (Low Risk) or Bad (High Risk). It demonstrates a complete MLOps workflow, from exploratory data analysis and model training to deployment as an interactive web application.

Objective: To build a robust classification model that aids financial institutions in automated risk assessment, minimizing potential losses.

Skills Demonstrated: Machine Learning (Classification), Data Preprocessing (Encoding), Model Selection & Tuning, Model Serialization (Joblib), and Web Application Deployment (Streamlit).

Key Achievement: Developed a highly accurate Random Forest Classifier and deployed it as a functional, real-time prediction tool.

**2. Problem Statement**

The core challenge is a binary classification problem: Given an applicant's demographic and financial information, the model must predict the probability that the applicant will default on their credit obligation. This prediction is simplified into a binary outcome: Good Credit Risk (0) or Bad Credit Risk (1).

**💾 3. Data & Features**

Dataset: German Credit Data (A standard dataset for credit risk modeling).
Target Variable: Risk (Binary: Good or Bad).
Key Features Used for Prediction (Input Variables):
* Age
* Sex
* Job
* Housing
* Saving accounts
* Checking account
* Credit amount
* Duration (of credit in months)

**🛠️ 4. Tools and Technologies **

Development Environment	-> Jupyter Notebook (Model Analysis.ipynb)	-> Data exploration, feature engineering, and model prototyping.
Core Language ->	Python 3.x	-> All scripting, modeling, and deployment logic.
ML Libraries ->	Scikit-learn, Joblib	-> Model building, training, evaluation, and serialization.
Data Manipulation	-> Pandas, NumPy	-> Data loading, cleaning, and preprocessing
Deployment ->	Streamlit (app.py)	-> Creating the interactive web application for real-time prediction.

**🚀 5. Machine Learning Pipeline**

A. Data Preprocessing & Feature Engineering 
    * Handling Categorical Data
    * Data Splitting

B. Model Selection and Training
    * Random Forest Classifier

C. Model Evaluation
    * Accuracy
    * Precision & Recall
    * Confusion Matrix

D. Model Serialization and Deployment
    * Model Saving
    * Web App Creation
