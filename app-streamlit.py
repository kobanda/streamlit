#imports
import pandas as pd
import streamlit as st
import plotly_express as px

#making a project in Titanic dashboard
st.set_page_config(layout="wide")
st.title("Titanic Dashboard")

# bring in titanic data
df = pd.read_csv('titani_data.csv')
#st.write(df.head())

#fill column called embarked with unknow for missing values
df.Embarked = df.Embarked.fillna('Unknown')
embarked_port =list( df.Embarked.unique())
gender = list(df.Sex.unique())

#create two colums
col1, col2 = st.columns([1,1])
with col1:
    st.selectbox(options = embarked_port,label="Select a Port")
with col2:
    st.selectbox(options = gender,label="Select a Gender")
