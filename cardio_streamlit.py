# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 17:24:24 2020

@author: Mandar Joshi
"""

import streamlit as st
import pandas as pd
import pickle
import numpy as np

st.header("Cardio Disease Prediction")

age = st.sidebar.number_input("Enter age in days")
age = int(age)
age = int(age/365)


height = st.sidebar.number_input("Enter height in CM")
height = int(height)

weight = st.sidebar.number_input("Enter weight in KG")
weight = int(weight)

ap_hi = st.sidebar.number_input("Enter Systolic blood pressure")
ap_hi = int(ap_hi)

ap_lo = st.sidebar.number_input("Enter Diastolic blood pressure")
ap_lo = int(ap_lo)


gender = st.radio("Select gender",('Male', 'Female'))
if gender=="Male":
    gender=1
else:
    gender=0


cholesterol = st.radio("Select Cholesterol level",('normal', 'above normal','well above normal'))

if cholesterol=="normal":
    cholesterol=1
elif cholesterol=='above normal':
    cholesterol=2
else:
    cholesterol=3

gluc = st.radio("Select Glucose level",('normal', 'above normal','well above normal'))

if gluc=="normal":
    gluc=1
elif gluc=='above normal':
    gluc=2
else:
    gluc=3

smoke = st.radio("Does patient smoke",('Yes','No'))

if smoke=="Yes":
    smoke=1
else:
    smoke=0

alco = st.radio("Alcohol intake",('Yes','No'))

if alco=="Yes":
    alco=1
else:
    alco=0

active = st.radio("Physical activity?",('Yes','No'))

if active=="Yes":
    active=1
else:
    active=0
    
a = np.zeros(shape=(1,11))
df = pd.DataFrame(a,columns=['age','height','weight','ap_hi','ap_lo','gender','cholesterol','gluc','smoke','alco','active'])
df['age'] = age 
df['height'] = height 
df['weight'] = weight 
df['ap_hi'] = ap_hi 
df['ap_lo'] = ap_lo 
df['gender'] = gender 
df['cholesterol'] = cholesterol 
df['gluc'] = gluc 
df['smoke'] = smoke 
df['alco'] = alco 
df['active'] = active 

st.dataframe(data=df)



if st.button('Show Dataframe'):
    st.write(df)
    
if st.button('Pred'):
    loaded_model = pickle.load(open("cardio.pickle1.dat", "rb"))
    y_pred = loaded_model.predict(df)[0]
    st.write(y_pred)
try:
    if y_pred==0:
        st.write('No cardiovascular disease')
        st.balloons()
    else:
        st.write('cardiovascular disease')
except:
    pass

data = st.file_uploader("Upload a Dataset", type=["csv", "txt"])

if st.button('Pred file'):
    try:
        loaded_model = pickle.load(open("pima.pickle1.dat", "rb"))
        df2 = pd.read_csv(data)
        y_pred = loaded_model.predict(df2)
        st.write(y_pred)
    except:
        st.wirte("file contain errors")
    


#st.dataframe(df)
