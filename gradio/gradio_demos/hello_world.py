import gradio as gr

from .base import GradioDemoBase


class HelloWorld(GradioDemoBase):
    @staticmethod
    def greet(name: str):
        return f"Hello {name}!"

    def render(self) -> gr.blocks.Blocks | gr.interface.Interface:
        demo = gr.Interface(fn=self.greet, inputs="textbox", outputs="textbox")
        return demo
