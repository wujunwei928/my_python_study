import gradio as gr
import numpy as np

from .base import GradioDemoBase


def sepia(input_img):
    sepia_filter = np.array([
        [0.393, 0.769, 0.189],
        [0.349, 0.686, 0.168],
        [0.272, 0.534, 0.131]
    ])
    sepia_img = input_img.dot(sepia_filter.T)
    sepia_img /= sepia_img.max()
    return sepia_img


class SepiaFilter(GradioDemoBase):
    def render(self) -> gr.blocks.Blocks | gr.interface.Interface:
        demo = gr.Interface(sepia, gr.Image(), "image")

        return demo
