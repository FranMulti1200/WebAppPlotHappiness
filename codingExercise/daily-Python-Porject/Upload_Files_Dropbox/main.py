import streamlit as st


st.title("Dropbox File Uploader")
st.subheader("Choose a file to upload")
st.file_uploader("Drag and drop file here")
st.text("File name: ")
st.text("File size: ")

st.button("Upload", on_click=None)
