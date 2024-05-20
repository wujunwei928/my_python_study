import time

import gradio as gr
import numpy as np

from .base import GradioDemoBase


def slow_echo(message, history):
    for i in range(len(message)):
        time.sleep(0.05)
        yield "You typed: " + message[: i + 1]


class StreamingChatbot(GradioDemoBase):
    def render(self) -> gr.blocks.Blocks | gr.interface.Interface:
        demo = gr.ChatInterface(slow_echo).queue()
        return demo
