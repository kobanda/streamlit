import mysql.connector
import streamlit as st

 #connection
con = mysql.connector.connect(
     host="localhost",
     port="3306",
     user="root",
     db="mydb"
 )
c= con.cursor()
#fetch data
def view_all_data():
    c.execute('select * from insurance order by id asc')
    data = c.fetchall()
    return data
