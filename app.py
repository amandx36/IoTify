import streamlit as st

# Page config
st.set_page_config(page_title="IoTify - Innovate. Build. Deliver.", layout="wide")

# Load CSS
with open("styles.css", "r", encoding="utf-8") as f:
    css_content = f"<style>{f.read()}</style>"

# Load JS
with open("script.js", "r", encoding="utf-8") as f:
    js_content = f"<script>{f.read()}</script>"

# Load HTML
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Replace external references with inline (so Streamlit can handle it)
html_content = html_content.replace(
    '<link rel="stylesheet" href="styles.css">', css_content
)
html_content = html_content.replace(
    '<script src="script.js"></script>', js_content
)

# Render inside Streamlit
st.components.v1.html(html_content, height=2000, scrolling=True)

