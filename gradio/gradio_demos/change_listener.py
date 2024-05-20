import gradio as gr
import numpy as np

from .base import GradioDemoBase


def welcome(name):
    return f"Welcome to Gradio, {name}!"


class ChangeListener(GradioDemoBase):
    def render(self) -> gr.blocks.Blocks | gr.interface.Interface:
        with gr.Blocks() as demo:
            gr.Markdown(
            """
            # Hello World!
            Start typing below to see the output.
            """)
            inp = gr.Textbox(placeholder="What is your name?")
            out = gr.Textbox()
            inp.change(welcome, inp, out)
        
        return demo
