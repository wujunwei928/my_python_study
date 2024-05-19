import streamlit as st

st.set_page_config(
    page_title="语音转文字",
    page_icon="🎧",
)

st.sidebar.title("🎧语音转文字")

st.page_link("pages/2_🍎_dev.py", icon="🌸", label="开发工具")

st.selectbox(
    "选择语音转文字的语言",
    ("中文", "英文")
)

st.selectbox(
    "选择语音转文字的音频格式",
    ("wav", "mp3")
)

st.slider(
    "音量",
    0, 100, (25, 75)
)

st.slider(
    "音高",
    0, 100, (25, 75)
)

st.slider(
    "语速",
    0, 100, (25, 75)
)


st.title("🎧语音转文字")




