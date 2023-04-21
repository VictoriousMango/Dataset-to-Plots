import streamlit as st

def app(show):
    st.title('Welcome User')
    SheetLink = st.text_input('Enter the Link of Google Sheets :')
    st.write(SheetLink)

if __name__ == '__main__' :
    show = True
    app(show)