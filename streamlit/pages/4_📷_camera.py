import streamlit as st

picture = st.camera_input("Take a picture")

if picture:
    # 显示图片
    st.image(picture)

    # To read image file buffer as bytes:
    bytes_data = picture.getvalue()
    # Check the type of bytes_data:
    # Should output: <class 'bytes'>
    st.write(type(bytes_data))
