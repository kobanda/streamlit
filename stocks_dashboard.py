import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache_data
def load_data():
    """Utility function"""
    df = pd.read_csv("all_stocks_5yr.csv",index_col='date')
    numeric_df = df.select_dtypes(['float','int'])
    numeric_cols = numeric_df.columns

    text_df = df.select_dtypes(['object'])
    text_cols = text_df.columns

    #stock column name
    stock_cols = df['Name']
    unique_stocks = stock_cols.unique()

    return df, numeric_cols,text_cols, unique_stocks

#call the function
df, numeric_cols,text_cols, unique_stocks = load_data()

#title of the dashboard
st.title('Stocks Dashboard')
#create a checkbox
check_box = st.sidebar.checkbox(label="Display Dataset")
if check_box:
    st.write(df)
    