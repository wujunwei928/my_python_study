import gradio as gr
import numpy as np

from .base import GradioDemoBase


class VideoIdentity(GradioDemoBase):
    def render(self) -> gr.blocks.Blocks | gr.interface.Interface:
        demo = gr.Interface(
            fn=lambda video: video,
            inputs=gr.Video(),
            outputs="playable_video",
        )
        return demo
