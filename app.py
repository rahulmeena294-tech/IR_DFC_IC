import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

# Set page configuration to wide layout for dashboards
st.set_page_config(
    page_title="DFC/NWR Interchange Optimizer",
    page_icon="🚂",
    layout="wide"
)

# Path to your uploaded HTML file
html_file_path = Path(__file__).parent / "nwr & dfc interchange.html"

try:
    # Read the HTML file content
    with open(html_file_path, "r", encoding="utf-8") as f:
        html_code = f.read()
        
    # Render the HTML/JS application inside Streamlit
    # height=900 sets the viewport height, scrolling=True allows internal scrollbars
    components.html(html_code, height=950, scrolling=True)

except FileNotFoundError:
    st.error("⚠️ HTML file not found in your repository!")
    st.info(
        "Please make sure your file **'nwr & dfc interchange.html'** "
        "is uploaded to the root directory of your GitHub repository."
    )