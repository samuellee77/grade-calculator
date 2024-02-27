import streamlit as st
import json
st.title('Grade Calculator')
data = {}
file = st.file_uploader('Upload past json file', type='json')
if file is not None:
    st.write('File uploaded successfully')
    data = json.loads(file.getvalue())
    st.write(data)

if st.button('create category'):
    st.write('Category created')