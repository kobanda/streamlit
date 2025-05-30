# we want to create a dashboard for the internet usage over different countries
#lets start by importing modules
import pandas as pd
import streamlit as st
import plotly_express as px
from streamlit import title

#confiture wide layout for the dashboard and write a title for the pro
st.set_page_config(layout="wide")
st.header("Internet Usage In different countries")

#bring in the data for analysis
df = pd.read_csv("share-of-individuals-using-the-internet.csv")
#i need data between the year 2000-2016
df = df[(df.Year>=2000) & (df.Year<=2016)]
df=df.sort_values("Year")
df2 = df.sort_values("Country")

#now we want to get unique values from the years
years = df.Year.unique()
counties = df2.Country.unique()

# select a Year to use
selected_year = st.selectbox(label="Year",options=years,index=0)
#create the columns
col1,col2 = st.columns([2,1])
df_plot = df[df.Year==selected_year]
#draw a graph for choropleth
plot = px.choropleth(data_frame=df_plot,
                     locations="Country",
                     locationmode="country names",
                     color="Individuals using the Internet (% of population)",
                     color_continuous_scale=px.colors.qualitative.Vivid,
                     title="Visual Showing the individuals who are using the internet"
                     )
#create histogram
hist_plot = px.histogram(data_frame=df_plot,
                    x="Individuals using the Internet (% of population)",
                    title="Internet usage across countries in the year: {}".format(selected_year)
                    )
#show the graph
col1.plotly_chart(plot)
col2.plotly_chart(hist_plot)
# lets add a sidebar
st.sidebar.subheader("Country Level Details")
#lets initialize a form
form = st.sidebar.form('form')
select_country = form.selectbox(label="Countries",
                         options=counties,
                         index=0)
submit = form.form_submit_button("Submit")
if submit:
    st.subheader("Country Level anaystics for {}".format(select_country))
    df_by_year_and_country = df[df["Country"]==select_country]
    line = px.line(data_frame=df_by_year_and_country,
                   x="Year",
                   y="Individuals using the Internet (% of population)",
                   title="Internet Usage over time in {}".format(select_country))
    st.plotly_chart(line)


