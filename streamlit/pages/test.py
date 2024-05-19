import streamlit as st
import pandas as pd

st.title("摄像头拍照")
picture = st.camera_input("拍照")
if picture:
    st.image(picture)

st.markdown("---")


st.title("文件上传")
uploaded_file = st.file_uploader(
    label="Choose a file",
    type=["png", "jpg", "jpeg"],
)
if uploaded_file:
    st.image(uploaded_file)
st.markdown("---")


st.title("超链接")
st.page_link("https://baidu.com", label="百度", icon="🌎")
st.page_link("https://google.com", label="谷歌", icon="🌍")
st.markdown("---")


st.title("颜色选择器")
color = st.color_picker("Pick a color")
if color:
    st.write(color)
st.markdown("---")


st.title("日期选择器")
input_date = st.date_input("Pick a date", format="YYYY-MM-DD",)
if input_date:
    st.write(input_date)
input_time = st.time_input("Pick a time")
if input_time:
    st.write(input_time)
st.markdown("---")

st.title("数据编辑器")
df = pd.DataFrame(
    [
       {"command": "st.selectbox", "rating": 4, "is_widget": True},
       {"command": "st.balloons", "rating": 5, "is_widget": False},
       {"command": "st.time_input", "rating": 3, "is_widget": True},
    ],
)
edited_df = st.data_editor(df)
favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
st.markdown(f"Your favorite command is **{favorite_command}** 🎈")
st.markdown("---")