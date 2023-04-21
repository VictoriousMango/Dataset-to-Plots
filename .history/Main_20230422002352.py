import streamlit as st
import pandas as pd
from IPython.display import display

def app(show):
    st.title('Welcome User')
    SheetLink = st.text_input('Enter the Link of Google Sheets :')
    st.write(SheetLink)
    df = pd.read.csv(SheetLink)
    display(df)

if __name__ == '__main__' :
    show = True
    app(show)