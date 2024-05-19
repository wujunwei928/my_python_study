import streamlit as st

from utils.encrypt import md5_encode, md5_encode_upper, base64_encode, base64_decode

st.set_page_config(
    page_title="开发工具",
    page_icon="🍎",
)

st.markdown("# 🍎开发工具")

# 初始化 session state
# 和 st.text_area中的 key 参数对应
if "input_text_val" not in st.session_state:
    st.session_state.input_text_val = ""

# 输入文本
input_text = st.text_area(
    # 出于可访问性的原因，您永远不应该设置一个空标签 （label=""），
    # 而是在需要时用label_visibility隐藏它。将来，我们可能会通过引发异常来禁止空标签。
    label="输入文本",

    # 标签的可见性。visible：标签可见。hidden：标签不可见。collapsed：标签和空格都不可见。
    # 如果为"hidden"，则标签不会显示，但小部件上方仍有空白区域（相当于 label=""）。
    # 如果为"collapsed"，则标签和空格都会被移除。默认值为"可见"。
    label_visibility="collapsed",

    # textarea的高度: 像素
    height=300,

    #
    key="input_text_val",
)

# 显示文本, 方便复制
if st.session_state.input_text_val:
    st.code(st.session_state.input_text_val, language="plaintext")


# 侧边栏: 相关功能按钮 及 回调函数 start


def md5_click():
    st.session_state.input_text_val = md5_encode(st.session_state.input_text_val)


def base64_encode_click():
    st.session_state.input_text_val = base64_encode(st.session_state.input_text_val)


def base64_decode_click():
    st.session_state.input_text_val = base64_decode(st.session_state.input_text_val)


def str_lower_click():
    st.session_state.input_text_val = st.session_state.input_text_val.lower()


def str_upper_click():
    st.session_state.input_text_val = st.session_state.input_text_val.upper()


md5_lower_btn = st.sidebar.button(label="MD5加密", on_click=md5_click)
base64_encode_btn = st.sidebar.button("base64加密", on_click=base64_encode_click)
base64_decode_btn = st.sidebar.button("base64解密", on_click=base64_decode_click)
str_lower_btn = st.sidebar.button("转小写", on_click=str_lower_click)
str_upper_btn = st.sidebar.button("转大写", on_click=str_upper_click)


# 侧边栏: 相关功能按钮 及 回调函数 end


