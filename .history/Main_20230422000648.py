import streamlit as st

def app(show):
    st.title('Welcome User')
    SheetLink = st.input_text('Enter the Link of Google Sheets :')

if __name__ == '__main__' :
    show = True
    app(show)