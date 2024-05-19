import json

import gradio as gr

from utils.encrypt import md5_encode, sha1_encode, base64_encode, base64_decode

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b


def to_upper_case(text):
    return text.upper()


def to_lower_case(text):
    return text.lower()


def format_json(input_text):
    try:
        parsed_json = json.loads(input_text)
        formatted_json = json.dumps(parsed_json, indent=4, ensure_ascii=False)
        return formatted_json
    except json.JSONDecodeError:
        return "Invalid JSON"



with gr.Blocks() as demo:
    gr.Markdown("# 多页面示例")
    with gr.Tabs():
        with gr.TabItem("开发工具"):
            gr.Markdown("## 开发工具")
            input_text_val = gr.TextArea("", label="输入文本")

            dev_button_list = [
                [("MD5加密", md5_encode), ("SHA1加密", sha1_encode)],
                [("base64加密", base64_encode), ("base64解密", base64_decode)],
                [("大写", to_upper_case), ("小写", to_lower_case)],
            ]
            for btn_items in dev_button_list:
                with gr.Row():
                    for btn in btn_items:
                        gr.Button(btn[0]).click(
                            btn[1],
                            inputs=[input_text_val],
                            outputs=input_text_val,
                        )

        with gr.TabItem("JSON格式化"):
            gr.Markdown("## JSON格式化")
            with gr.Row():
                input_text = gr.Textbox(lines=10, label="输入 JSON")
                output_text = gr.Textbox(lines=10, label="格式化 JSON")
            format_button = gr.Button("格式化").click(
                format_json, inputs=[input_text], outputs=output_text
            )


demo.launch()
