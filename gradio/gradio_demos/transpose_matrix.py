import gradio as gr
import numpy as np

from .base import GradioDemoBase


class TransposeMatrix(GradioDemoBase):
    def render(self) -> gr.blocks.Blocks | gr.interface.Interface:
        demo = gr.Interface(
            lambda matrix: matrix.T,
            gr.Dataframe(type="numpy", datatype="number", row_count=5, col_count=3),
            "numpy",
            examples=[
                [np.zeros((3, 3)).tolist()],
                [np.ones((2, 2)).tolist()],
                [np.random.randint(0, 10, (3, 10)).tolist()],
                [np.random.randint(0, 10, (10, 3)).tolist()],
                [np.random.randint(0, 10, (10, 10)).tolist()],
            ],
            cache_examples=False
        )
        return demo
