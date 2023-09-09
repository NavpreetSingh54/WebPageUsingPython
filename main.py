import streamlit as st
#import pandas as pd
# st.title("Welcome to First Page")
#st.header("Python")
#st.subheader("Java")
#st.markdown("I Love Java")
#st.code(""" for i in range(1,5,1):
#print("Hello")
#""")
#dataset = pd.read_csv("annual.csv")
#st.dataframe(dataset)
name=st.text_input("Enter Your Name : ")
fname=st.text_input("Enter Your Father's Name : ")
adrs=st.text_area("Enter Your Text : ")
classdata=st.selectbox("Enter Your Class",(1,2,3,4,5,6,7,8,9,10,11,12))
button=st.button("Done")
if button :
  st.markdown(f"""
  Name:{name}
  Father Name:{fname}
  Text :{adrs}
  Class :{classdata}
  """)