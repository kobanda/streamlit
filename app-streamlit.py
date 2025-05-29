#imports
from itertools import groupby

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
selected_port = col1.selectbox(options = embarked_port,label="Select a Port")
selected_gender=col2.selectbox(options = gender,label="Select a Gender")

#filter using the selected port and gender
df_plot = df[df.Embarked==selected_port]
df_plot = df_plot[df.Sex==selected_gender]
#st.write(df_plot.head())

#plot
plot = px.histogram(data_frame=df_plot,
                    template="seaborn",
                    color="Survived",
                    title="Distribution of Age",
                    facet_col="Survived",
                    x="Age"
                    )
(col1.plotly_chart(plot))
df_plot_pie= df_plot.loc[:,['PassengerId','Survived']].groupby(['Survived']).count()

df_plot_pie.rename({'PassengerId':'Count of Passengers'},inplace=True,axis='columns')
st.write(df_plot_pie)
pie = px.pie(data_frame=df_plot_pie,
             template="seaborn",
             values="Count of Passengers",
             title="Count of Passengers that survived",
             names="Survived"
             )
st.plotly_chart(pie)
