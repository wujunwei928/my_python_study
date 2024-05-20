import time

import gradio as gr
import numpy as np

from .base import GradioDemoBase


def fake_diffusion(steps):
    rng = np.random.default_rng()
    for i in range(steps):
        time.sleep(1)
        image = rng.random(size=(600, 600, 3))
        yield image
    image = np.ones((1000, 1000, 3), np.uint8)
    image[:] = [255, 124, 0]
    yield image


class IterativeOutput(GradioDemoBase):
    def render(self) -> gr.blocks.Blocks | gr.interface.Interface:
        demo = gr.Interface(
            fn=fake_diffusion,
            inputs=gr.Slider(1, 10, 3, step=1),
            outputs="image",
        )
        return demo
