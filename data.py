import streamlit as st

st.title("MADE BY ISMAIL KHAN")
name = st.text_input("ENTER YOUR NAME : ")
fathername = st.text_input("ENTER YOUR FATHER NAME : ")
bio = st.text_area("ENTER YOUR TEXT : ")
classdata = st.selectbox("ENTER YOUR CLASS :",(1,2,3,4,5,6,7,8,9,10,11,12))

button = st.button("Done")
if button :
    st.markdown(f"""
    Name : {name}
    Father Name : {fathername}
    Text : {bio}
    Class : {classdata}""")
