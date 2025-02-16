from flask import Flask, request, jsonify, render_template
import numpy as np 
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn import svm

app = Flask(__name__)

# Assuming you have fetched the input data from SQL and stored it in a variable named 'input_data'
# Replace the placeholders with your SQL retrieval method

# Correcting the CSV file path based on your actual file path
loan_dataset = pd.read_csv(r'C:\Users\sarag\InnoFund\train_u6lujuX_CVtuZ9i (1).csv')

loan_dataset = loan_dataset.dropna()
loan_dataset.isnull().sum()

pd.set_option('future.no_silent_downcasting', True)  # Opting in to future behavior
loan_dataset.replace({"Loan_Status":{'N':0,'Y':1}}, inplace=True)
loan_dataset = loan_dataset.infer_objects()

loan_dataset['Dependents'].value_counts()
loan_dataset = loan_dataset.replace(to_replace='3+', value=4)
loan_dataset.replace({'Married':{'No':0,'Yes':1},'Gender':{'Male':1,'Female':0},'Self_Employed':{'No':0,'Yes':1},
                      'Property_Area':{'Rural':0,'Semiurban':1,'Urban':2},'Education':{'Graduate':1,'Not Graduate':0}}, inplace=True)
loan_dataset = loan_dataset.infer_objects()

X = loan_dataset.drop(columns=['Loan_ID','Loan_Status'], axis=1)
Y = loan_dataset['Loan_Status']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1, stratify=Y, random_state=2)

classifier = svm.SVC(kernel='linear')
classifier.fit(X_train, Y_train)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict_loan_approval():
    data = request.form  # Assuming input from a form
    input_data = [data['married'], data['dependents'], data['education'], data['self_employed'], 
                  data['applicant_income'], data['coapplicant_income'], data['loan_amount'], 
                  data['loan_amount_term'], data['credit_history'], data['property_area'], data['gender']]
    input_array = np.array(input_data).reshape(1, -1)

    # Predicting using the trained model
    prediction = classifier.predict(input_array)

    if prediction[0] == 1:
        result = "Loan Approved"
    else:
        result = "Loan Not Approved"

    return render_template('predict.html', prediction_text='Prediction: {}'.format(result))

if __name__ == '__main__':
    app.run(debug=True)
