import streamlit as st

# Set page config
st.set_page_config(page_title="IoTify - Innovate. Build. Deliver.", layout="wide")

# Load HTML file
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Display the HTML file inside Streamlit
st.components.v1.html(html_content, height=1200, scrolling=True)
