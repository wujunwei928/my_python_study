import gradio as gr

from .base import GradioDemoBase


class HelloBlocks(GradioDemoBase):
    @staticmethod
    def greet(name: str):
        return f"Hello {name}!"

    def render(self) -> gr.blocks.Blocks | gr.interface.Interface:
        with gr.Blocks() as demo:
            name = gr.Textbox(label="Name")
            output = gr.Textbox(label="Output Box")
            greet_btn = gr.Button("Greet")
            greet_btn.click(fn=self.greet, inputs=name, outputs=output, api_name="greet")
        return demo
