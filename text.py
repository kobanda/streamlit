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
text_area = st.text_area(label = "This is text area",
                         max_chars=1000,
                         placeholder = "Write your text here",
                         key="text_area",
                         help = "This is multi-line text area"
                         )

