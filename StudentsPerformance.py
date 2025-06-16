import sys
import pandas as pd 
import numpy as np 
import streamlit as st
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
st.header('predict the writing score')
st.sidebar.header('user inputs')
def user():
    gender=st.sidebar.selectbox('gender',('male','female'))
    race=st.sidebar.selectbox('race',('group A', 'group B', 'group C', 'group D', 'group E'))
    education=st.sidebar.selectbox('parent education',("bachelor's degree", 'some college', "master's degree",
       "associate's degree", 'high school', 'some high school'))
    lunch=st.sidebar.selectbox('lunch',('standard', 'free/reduced'))
    test=st.sidebar.selectbox('test preparation',('none','completed'))
    math_score=st.sidebar.slider('math_score',0,100)
    reading_score=st.sidebar.slider('reading_score',17,100)
    dat={
     'gender':gender,'race/ethnicity':race,'parental level of education':education,'lunch':lunch,'test preparation course':test,
     'math score':math_score,'reading score':reading_score}
    features=pd.DataFrame(dat,index=[0])
    return features
    #ad=pickle.load(open('student.pkl','rb'))
    #=load.predict(dat.values().reshape(1,-1))
    #=pd.DataFrame(da,columns=['writing score'])   
    #.write(da)

df=user()
data=pd.read_csv('C:\\Users\\Administrator\\Downloads\\students\\StudentsPerformance.csv')
stu=data.drop(columns='writing score')
con=pd.concat([df,stu],axis=0)
encode=['gender', 'race/ethnicity', 'parental level of education', 'lunch',
'test preparation course']
for c in encode:
     dummy=pd.get_dummies(con[c],prefix=c)
     con=pd.concat([con,dummy],axis=1)
     del con[c]
con=con[:1]
load=pickle.load(open('C:\\Users\\Administrator\\Downloads\\students\\student.pkl','rb'))
pred=load.predict(con)
if st.button('predict'):
    st.write('writing score')
    st.info('{:.0f}'.format(round(pred.item())))