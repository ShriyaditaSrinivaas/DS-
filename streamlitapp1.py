import streamlit as st
st.title("welocome to my app")
image_file=st.file_uploader("upload image here",type=['jpg','png','jpeg'])
st.image([image_file])