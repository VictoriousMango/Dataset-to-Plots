import streamlit as st
import pandas as pd
#from IPython.display import display

def app(show):
    st.title('Welcome User')
    SheetLink = st.text_input('Enter the Link of Google Sheets :')
    st.write(SheetLink)
    sheetlink = 'https://docs.google.com/spreadsheets/d/1SS5CyRoFk9t7lm7ZYg0vup1Nkp1NJqUV4j3Y1r8J5dM/export?foramt=csv'
    df = pd.read_csv(SheetLink)
    print(df)

if __name__ == '__main__' :
    show = True
    app(show)