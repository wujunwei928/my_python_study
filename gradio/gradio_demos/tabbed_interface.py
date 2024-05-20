import gradio as gr
import numpy as np

from .base import GradioDemoBase


class TabbedInterface(GradioDemoBase):
    def render(self) -> gr.blocks.Blocks | gr.interface.Interface:
        hello_world = gr.Interface(lambda name: "Hello " + name, "text", "text")
        bye_world = gr.Interface(lambda name: "Bye " + name, "text", "text")

        demo = gr.TabbedInterface([hello_world, bye_world], ["Hello World", "Bye World"])
        return demo
