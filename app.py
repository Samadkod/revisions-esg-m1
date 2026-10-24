from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Révisions ESG M1", page_icon="📚", layout="wide")

# Masque l'en-tête/pied Streamlit et retire les marges pour laisser toute la place à l'appli
st.markdown(
    """
    <style>
      #MainMenu, header, footer {visibility: hidden;}
      .block-container {padding: 0 !important; max-width: 100% !important;}
      iframe {display: block;}
    </style>
    """,
    unsafe_allow_html=True,
)

html = (Path(__file__).parent / "static" / "index.html").read_text(encoding="utf-8")
components.html(html, height=1000, scrolling=True)
