import pandas as pd
import numpy as np


ld=pd.read_csv('/content/credit - credit (4).csv')

#Outliers
q1=np.percentile(cs['Annual_Income'],25,method='midpoint')
q2=np.percentile(cs['Annual_Income'],50,method='midpoint')
q3=np.percentile(cs['Annual_Income'],75,method='midpoint')
IQR=q3-q1
low_lim=q1-1.5*IQR
up_lim=q3+1.5*IQR
cs['Annual_Income']=cs['Annual_Income'].clip(lower=low_lim,upper=up_lim)


q1=np.percentile(cs['Delay_from_due_date'],25,method='midpoint')
q2=np.percentile(cs['Delay_from_due_date'],50,method='midpoint')
q3=np.percentile(cs['Delay_from_due_date'],75,method='midpoint')
IQR=q3-q1
low_lim=q1-1.5*IQR
up_lim=q3+1.5*IQR
cs['Delay_from_due_date']=cs['Delay_from_due_date'].clip(lower=low_lim,upper=up_lim)

q1=np.percentile(cs['Outstanding_Debt'],25,method='midpoint')
q2=np.percentile(cs['Outstanding_Debt'],50,method='midpoint')
q3=np.percentile(cs['Outstanding_Debt'],75,method='midpoint')
IQR=q3-q1
low_lim=q1-1.5*IQR
up_lim=q3+1.5*IQR
cs['Outstanding_Debt']=cs['Outstanding_Debt'].clip(lower=low_lim,upper=up_lim)

q1=np.percentile(cs['Total_EMI_per_month'],25,method='midpoint')
q2=np.percentile(cs['Total_EMI_per_month'],50,method='midpoint')
q3=np.percentile(cs['Total_EMI_per_month'],75,method='midpoint')
IQR=q3-q1
low_lim=q1-1.5*IQR
up_lim=q3+1.5*IQR
cs['Total_EMI_per_month']=cs['Total_EMI_per_month'].clip(lower=low_lim,upper=up_lim)

q1=np.percentile(cs['Amount_invested_monthly'],25,method='midpoint')
q2=np.percentile(cs['Amount_invested_monthly'],50,method='midpoint')
q3=np.percentile(cs['Amount_invested_monthly'],75,method='midpoint')    
IQR=q3-q1
low_lim=q1-1.5*IQR
up_lim=q3+1.5*IQR
cs['Amount_invested_monthly']=cs['Amount_invested_monthly'].clip(lower=low_lim,upper=up_lim)

q1=np.percentile(cs['Monthly_Balance'],25,method='midpoint')
q2=np.percentile(cs['Monthly_Balance'],50,method='midpoint')
q3=np.percentile(cs['Monthly_Balance'],75,method='midpoint')
IQR=q3-q1
low_lim=q1-1.5*IQR
up_lim=q3+1.5*IQR
cs['Monthly_Balance']=cs['Monthly_Balance'].clip(lower=low_lim,upper=up_lim)

#Label encoding
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()


cs['Credit_Score']=le.fit_transform(cs['Credit_Score'])

#Test & train data
y = cs['Credit_Score']
x = cs.drop(columns=['Credit_Score'])
from sklearn.model_selection import train_test_split
x_train,x_temp,y_train,y_temp=train_test_split(x,y,random_state=42,test_size=0.25)

#model random forest
from sklearn.ensemble import RandomForestClassifier
rf_clf=RandomForestClassifier()
rf_clf.fit(X_train,y_train)
pred=rf_clf.predict(x_test)

#create pickle
import pickle
with open('model1.pkl','wb') as model1_file:  
    pickle.dump(rf_clf,model1_file)  
