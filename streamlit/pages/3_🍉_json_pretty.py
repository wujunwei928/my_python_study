import streamlit as st

st.set_page_config(
    page_title="json pretty",
    page_icon="🍉",
)

st.title("🍉json pretty")

input_json = st.text_area(label="输入json")

if input_json:
    st.json(input_json)

