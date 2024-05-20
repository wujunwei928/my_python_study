import random

import gradio as gr
import numpy as np

from .base import GradioDemoBase


def random_response(message, history):
    return random.choice(["Yes", "No"])


class Chatbot(GradioDemoBase):
    def render(self) -> gr.blocks.Blocks | gr.interface.Interface:
        demo = gr.ChatInterface(random_response)
        return demo
