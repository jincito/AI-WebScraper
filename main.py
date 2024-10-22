# Streamlit User Interface -
# interacting with LLMs using simple python web application
import streamlit as st
from scrape import scrape_website

st.title("AI Web Scraper")
url = st.text_input("Enter a Website URL: ")

if st.button("Scrape Site"):
    st.write("Scraping Site...")
    result = scrape_website(url)
    print(result)
    # Display the results in a table or list
    # st.write(results)
