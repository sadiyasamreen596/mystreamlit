import streamlit as st
st.title('Sadiya')
st.header('hello everyone')

st.text('This is an online course')
st.markdown('<center><h1>Welcome</h1></center>',unsafe_allow_html=True)

mymenu=st.sidebar.selectbox('My.Menu',('Home','FillForm','Download'))
st.video('https://www.youtube.com/watch?v=paQoaPQNgAE')
                      
