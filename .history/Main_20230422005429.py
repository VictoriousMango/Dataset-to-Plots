import streamlit as st
import pandas as pd
#from IPython.display import display

def app(show):
    st.title('Welcome User')
    uploaded_file = st.file_uploader('Choose a file')
    if uploaded_file is not None:
        #read csv
        df1=pd.read_csv(uploaded_file)

        #read xls or xlsx
        df1=pd.read_excel(uploaded_file)
    else:
        st.warning('you need to upload a csv or excel file.')

if __name__ == '__main__' :
    show = True
    app(show)