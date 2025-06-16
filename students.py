import streamlit as at 
import pickle
import pandas as pd
dataa=pd.read_csv('StudentsPerformance.csv')
data=dataa.copy()
target='writing score'
encode=['gender', 'race/ethnicity', 'parental level of education', 'lunch',
'test preparation course']
for c in encode:
    dummy=pd.get_dummies(data[c],prefix=c)
    data=pd.concat([data,dummy],axis=1)
    del data[c]
x=data.drop(columns='writing score')
y=data['writing score']
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,
                                            random_state=42)
from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(x_train,y_train)
pickle.dump(model,open('student.pkl','wb'))