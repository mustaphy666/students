import sys
import pandas as pd 
import numpy as np 
import streamlit as st
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
st.title('Writing score app prediction')
st.write('**This app predict the writing score by tuning the user inputs parameters**')
st.subheader('User inputs')
def user():
    gender=st.selectbox('Gender',('male','female'))
    race=st.selectbox('Race',('Black', 'Asian', 'European', 'indigenous people', 'pacific islander'))
    education=st.selectbox('Parent education',("bachelor's degree", 'some college', "master's degree",
       "associate's degree", 'high school', 'some high school'))
    lunch=st.selectbox('Lunch',('standard', 'free/reduced'))
    test=st.selectbox('Test preparation',('none','completed'))
    math_score=st.slider('Math score',0,100)
    reading_score=st.slider('Reading score',17,100)
    dat={
     'gender':gender,'race':race,'parental level of education':education,'lunch':lunch,'test preparation course':test,
     'math score':math_score,'reading score':reading_score}
    features=pd.DataFrame(dat,index=[0])
    return features
df=user()
data=pd.read_csv('StudentsPerformance.csv')
<<<<<<< HEAD
race={'group A':'Black','group B':'Asian','group C':'European','group D':'pacific islander','group E':'indigenous people'}
data['race']=data['race/ethnicity'].map(race)
stu=data.drop(columns=['writing score','race/ethnicity'])
=======
stu=data.drop(columns='writing score')
>>>>>>> 7cc045838cd95dfa799806cde33c2b722fc0cff7
con=pd.concat([df,stu],axis=0)
encode=['gender', 'race', 'parental level of education', 'lunch',
'test preparation course']
for c in encode:
     dummy=pd.get_dummies(con[c],prefix=c)
     con=pd.concat([con,dummy],axis=1)
     del con[c]
con=con[:1]
load=pickle.load(open('student.pkl','rb'))
pred=load.predict(con)
if st.button('predict'):
    st.write('writing score')
    st.info('{:.0f}'.format(round(pred.item())))
