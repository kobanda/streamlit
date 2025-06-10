import streamlit as st
import pandas as pd
import plotly_express as px

#lets add title to the page
st.title("Data Visualization App")
#add a subheader at the sidebar
st.sidebar.subheader("Visualization Settings")

#create file uploader
file_upload= st.sidebar.file_uploader(
    label="Please upload csv or excel file here",
    type=['csv','xlsx']
)
#check whether to display dataset or not
display_dataset = st.sidebar.checkbox(
    label="Would you like to display the uploaded dataset?"
)
print(file_upload)
#declare global variables to be accessible everywhere in the program
global df
global numeric_cols
global non_numeric_cols
global select_chart
#account for cases where uploaded file is not none
if file_upload is not None: #when file is not yet uploaded
    # try:
    df = pd.read_csv(file_upload)
    #reset buffer
    file_upload.seek(0)
    # except Exception as e:
    #     print(e)
    #     df = pd.read_excel(file_upload)
    if display_dataset:
        st.write(df)

    #we want to extract numeric columns as list
    numeric_cols = list(df.select_dtypes(['float','int']).columns)

    #extract non-numeric columns as a list
    non_numeric_cols = list(df.select_dtypes(['object']).columns)

    #append None value to non-numeric list
    non_numeric_cols.append('None')
    # st.write(numeric_cols)
    # st.write(non_numeric_cols)

    #add visualization widget
    select_chart = st.sidebar.selectbox(
        label="Select visualization type",
        options=["Histogram","Lineplot","Scatterplot"]
    )
    print(select_chart)
try:
    # use the chat selected to draw graph
    if select_chart=="Scatterplot":
        st.sidebar.subheader("Setting for Scatterplot")
        x_value = st.sidebar.selectbox(
            label="X-Axis",
            options=numeric_cols
        )
        y_value = st.sidebar.selectbox(
            label="Y-Axis",
            options=numeric_cols
        )
        #check if user wants to specify color
        specify_color = st.sidebar.checkbox(
            label="Would you want to specify the color?"
        )
        if specify_color:
            #color coding the chart
            color_value = st.sidebar.selectbox(
                label = "Select Color",
                options=non_numeric_cols
            )
            #draw the scatterplot
            plot =px.scatter(
                data_frame=df,
                x=x_value,
                y=y_value,
                color=color_value
            )
        else:
            plot =px.scatter(
                data_frame=df,
                x=x_value,
                y=y_value
            )
            # display the chart
            st.plotly_chart(plot)
    if select_chart == "Histogram":
        st.sidebar.subheader("Setting for Histogram")
        x_value = st.sidebar.selectbox(
            label="Feature",
            options=numeric_cols
        )
        bin_size = st.sidebar.slider(
            label="Number of Bins",
            min_value=10,
            max_value=100,
            value=50
        )
        plot = px.histogram(
            data_frame=df,
            x=x_value,
            nbins=bin_size
        )
        st.plotly_chart(plot)
    if select_chart == "Lineplot":
        st.sidebar.subheader("Setting for Lineplot")
        x_value = st.sidebar.selectbox(label="X-Axis",options=numeric_cols)
        y_value = st.sidebar.selectbox(label="Y-Axis",options=numeric_cols)

        #plot line
        plot = px.line(data_frame=df,x=x_value,y=y_value)
        #display the chart
        st.plotly_chart(plot)
except Exception as e:
    print(e)
