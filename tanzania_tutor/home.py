import time
from logging import currentframe

import streamlit as st
import pandas as pd
import plotly_express as px
from numerize.numerize import numerize
import time

from streamlit_option_menu import option_menu

#from query import *

#set the page configuration
st.set_page_config(page_title="Dashboard", page_icon="🌍",layout="wide")
st.markdown(
    "<h3 style='text-align: center;'>🔔 System for Descriptive Data Analysis</h3>",
    unsafe_allow_html=True
)

#fetch the data
#result = view_all_data()
#df=pd.DataFrame(result,columns=["policy","Expiry","Location","State","Region","Investment","Construction","BusinessType","Earthquake","Flood","Rating","ID"])
#make a sidebar with logo
st.sidebar.image("coeLogo.png",width=200)
df=pd.read_csv("data.csv")
#making switchers
st.sidebar.header("Please filter")

region = st.sidebar.multiselect(label = "Select a region",
                                options=df.Region.unique(),
                                default=df.Region.unique()
                                )
location = st.sidebar.multiselect(label = "Select a location",
                                options=df.Location.unique(),
                                default=df.Location.unique()
                                )
construction = st.sidebar.multiselect(label = "Select a Construction",
                                options=df.Construction.unique(),
                                default=df.Construction.unique()
                                )
#handle error of no selection made
if not region:
    st.sidebar.warning("Please select at least one Region")
if not location:
    st.sidebar.warning("Please select at least one Location")
if not construction:
    st.sidebar.warning("Please select at least one Construction")
#this query selected and unselected the data from the dataset
df_selection = df.query(
    "Region==@region & Location==@location & Construction==@construction"
)
#st.dataframe(df_selection)

#now we make an expander to display the dataframe
#make a function
def Home():
    with st.expander("Tabular"):
        showData = st.multiselect("Filter",df_selection.columns,default=[])
        st.write(df_selection[showData])

    #want to computer the top analytics, metrics
    total_investment = df_selection.Investment.sum()
    mode_investment = df_selection.Investment.mode()
    mean_investment = df_selection.Investment.mean()
    median_investment = df_selection.Investment.median()
    rating = df_selection.Rating.sum()

    #creat columns
    col1,col2,col3,col4,col5 = st.columns(5,gap="large")
    try:
        if not df_selection.empty:
            with col1: #total investment
                st.info("Total Investment",icon="📌")
                st.metric(label="Sum Ksh.", value=f"{total_investment:,.0f}")
            with col2: #mode
                st.info("Most Frequent",icon="📌")
                st.metric(label="Mode Ksh.", value=mode_investment)
            with col3: #mean
                st.info("Average Investment",icon="📌")
                st.metric(label="Mean Ksh.", value=f"{mean_investment:,.0f}")
            with col4: #median
                st.info("Central Earnings",icon="📌")
                st.metric(label="Median Ksh.", value=f"{median_investment:,.0f}")
            with col5: #rating
                st.info("Ratings Investment",icon="📌")
                st.metric(label="Rating Ksh.", value=numerize(rating),help=f""" Total Rating {rating} """)
            st.markdown("""___""")
        else:
            st.warning("No metrics to display. Please adjust your filters.")
    except Exception:
        st.warning("Something went wrong while processing your data. Please adjust filters.")
        print(f"Error occured")
        traceback.print_exc()
#now we need the function for creating graphs
def graphs():
    total_investment = df_selection.Investment.sum()
    averageRating = round(df_selection.Rating.mean(),2)

    #simple  bar graph for investment by Business Type
    investment_by_business_type = df_selection.groupby(by=["BusinessType"]).count()[["Investment"]].sort_values(by="Investment")
    fig_investment = px.bar(
        data_frame = investment_by_business_type,
        x = "Investment",
        y = investment_by_business_type.index,
        orientation="h",
        title="<b>Investment by Business Type</b>",
        color_discrete_sequence=["#083b88"]*len(investment_by_business_type),
        template="plotly_white"
    )
    fig_investment.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis = (dict(showgrid=False))
    )
    # simple  bar graph for investment by State
    investment_by_state = df_selection.groupby(by=["State"]).count()[["Investment"]].sort_values(by="State")
    fig_state = px.line(
        data_frame=investment_by_state,
        x=investment_by_state.index,
        y="Investment",
        orientation="h",
        title="<b>Investment by State</b>",
        color_discrete_sequence=["#083b88"] * len(investment_by_state),
        template="plotly_white"
    )
    fig_state.update_layout(
        xaxis=dict(tickmode="linear"),
        plot_bgcolor="rgba(0,0,0,0)"
    )
    #create columns to put the graphs
    left,right = st.columns(2)
    left.plotly_chart(fig_state,use_container_width=True)
    right.plotly_chart(fig_investment,use_container_width=True)

    #now we create a progress bar
def ProgressBar():
    st.markdown("""<style>.stProgress> div>div>div>div { background-image:linear-gradient(to right, #99ff99, #FFFF00)}</style>""",unsafe_allow_html=True)
    target=3000000000
    current=df_selection["Investment"].sum()
    percent=round((current/target)*100)
    mybar=st.progress(0)

    if percent>100:
        st.subheader("Target Done!")
    else:
        st.write("You have",percent,"% ","of ",(format(target,"d")),"Ksh")
        for percent_complete in range(percent):
            time.sleep(0.1)
            mybar.progress(percent_complete+1,text="Target Percentage")
def sidebar():
    with st.sidebar:
        selected = option_menu(
            menu_title="Main Menu",
            options=["Home","Progress"],
            icons=["house","eye"],
            menu_icon="cast",
            default_index=0
        )
    if selected=="Home":
        st.subheader(f"Page: {selected}")
        Home()
        graphs()
    if selected=="Progress":
        st.subheader(f"Page: {selected}")
        ProgressBar()
        graphs()
sidebar()

#theme
hide_st_style="""
<style>
#MainMenu{visibility:hidden;}
footer{visibility:hidden}
header{visibility:hidden}
</style
"""