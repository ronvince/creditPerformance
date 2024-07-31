from flask import Flask, request, render_template, jsonify
import pickle
import pandas as pd
import numpy as np

from decompress import decompress_model

#ld=pd.read_csv('/content/credit - credit (4).csv')

app = Flask(__name__)

model = decompress_model()


@app.route('/home',methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    data = request.json

    # Extract each value from the JSON
    annual_income = data.get('annual_income')
    delay_from_due_date = data.get('delay_from_due_date')
    changed_credit_limit = data.get('changed_credit_limit')
    outstanding_debt = data.get('outstanding_debt')
    credit_utilization_ratio = data.get('credit_utilization_ratio')
    credit_history_age = data.get('credit_history_age')
    total_emi_per_month = data.get('total_emi_per_month')
    amount_invested_monthly = data.get('amount_invested_monthly')
    monthly_balance = data.get('monthly_balance')
    
    # Optional: Handle a non-existent or additional field
   # age_group = data.get('age_group', None)

    # Create DataFrame from form data
    cs = pd.DataFrame({
        'Annual_Income': [float(annual_income)],
        'Delay_from_due_date': [float(delay_from_due_date)],
        'Changed_Credit_Limit': [float(changed_credit_limit)],
        'Outstanding_Debt': [float(outstanding_debt)],
        'Credit_Utilization_Ratio': [float(credit_utilization_ratio)],
        'Credit_History_Age': [float(credit_history_age)],
        'Total_EMI_per_month': [float(total_emi_per_month)],
        'Amount_invested_monthly': [float(amount_invested_monthly)],
        'Monthly_Balance': [float(monthly_balance)],
       # 'Age Group': [float(age_group)]
        
    })
    prediction = model1.predict(cs)
    #prediction_='Good' if prediction[0]== 1 else 'Standard' if prediction[1]==1 else 'Poor'
    if prediction[0]==0: 
        credit_performance='Good'
    elif prediction[0]==1:
       credit_performance='Standard'
    else:
        credit_performance='Poor'   
    #return render_template('result.html',pred=prediction)
    return jsonify({'prediction': credit_performance})    

if __name__ == '__main__':
    app.run(debug=True)