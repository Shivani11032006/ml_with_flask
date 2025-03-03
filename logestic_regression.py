import pandas as pd
import streamlit as st
from sklearn.linear_model import LogisticRegression

def user_input_features():
    CLMSEX = st.sidebar.selectbox('Gender', ('1', '0'))
    CLMINSUR = st.sidebar.selectbox('Insurance', ('1', '0'))
    SEATBELT = st.sidebar.selectbox('Seatbelt', ('1', '0'))
    CLMAGE = st.sidebar.number_input('Insert Age')
    LOSS = st.sidebar.number_input('Insert Loss')
    data = {
        'CLMSEX': CLMSEX,
        'CLMINSUR': CLMINSUR,
        'SEATBELT': SEATBELT,
        'CLMAGE': CLMAGE,
        'LOSS': LOSS
    }
    features = pd.DataFrame(data, index=[0])
    return features

# Get user input
df = user_input_features()

# Display user input parameters
st.subheader('User Input parameters')
st.write(df)

# Load data
claimants = pd.read_csv('claimants2.csv')
claimants.drop(['CASENUM'], inplace=True, axis=1)
claimants = claimants.dropna()

# Split data into predictors (X) and target (Y)
X = claimants.iloc[:, [1, 2, 3, 4, 5]]
Y = claimants.iloc[:, 0]

# Train the logistic regression model
clf = LogisticRegression()
clf.fit(X, Y)

# Make predictions
prediction = clf.predict(df)
prediction_prob = clf.predict_proba(df)

# Display results
st.subheader('Predicted Result')
st.write('Yes' if prediction_prob[0][1] > 0.5 else 'No')

st.subheader('Prediction Probability')
st.write(prediction_prob)