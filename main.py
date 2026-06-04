import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error
st.title("HOUSE PRICE PREDCITION")
data=pd.read_csv("LINEAR.csv")
# print(data.columns)

X=data[['Hours_Studied']]
y=data['Exam_Score']
X_train,X_test,y_train,y_test=train_test_split(X,y)
model=LinearRegression()
model.fit(X_train,y_train)
sq=st.number_input("Enter sqft")
bt=st.button("Submit")
bt1=st.button("evalution")
if bt:
    out=model.predict([[sq]])
    st.write(out)
if bt1:
    out=model.predict(X_test)
    mae=mean_absolute_error(y_test,out)
    mse=mean_squared_error(y_test,out)
    r2=r2_score(y_test,out)
    st.write(mae,mse,r2)
