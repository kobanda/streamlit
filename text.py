import streamlit as st


st.title("Streamlit text Widget Lesson")
col1,col2 = st.columns([1,1])
text_input = col1.text_input(label="Enter your text",
                           placeholder="Type here...",
                           max_chars=100,
                           key="text_input")
if text_input:
    col1.write("Your entered: {}".format(text_input))
text_passowrd = col2.text_input(label = "Enter your Password",
                             type = "password",
                             placeholder = "Type here...",
                              max_chars=10,
                             key = "tex_password"
                             )
#the text area
text_area = col1.text_area(label = "This is text area",
                         max_chars=1000,
                         placeholder = "Write your text here",
                         key="text_area",
                         help = "This is multi-line text area"
                         )

#lets do number input
number_input = st.sidebar.number_input(label="Enter a number",
                               max_value=100,
                               min_value=0,
                               value=50,
                               step=1,
                               help="Use this widget to input a number"
                               )
st.sidebar.write(f"The number is: ",number_input)
#lets now learn pills
cities = ["Siaya","Nairobi","Kisumu","Mombasa","Nakuru","London","America"]
selected_city = col2.pills(label="Select a city",
                 options=cities,
                 selection_mode="multi",
                 help="Pick your faviourite city",
                 key="city1"
                 )
#print the selected city
col2.write("The city selected is: {}".format(selected_city))