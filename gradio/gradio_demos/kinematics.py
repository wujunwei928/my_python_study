import gradio as gr
import numpy as np
import pandas as pd

from .base import GradioDemoBase


def plot(v, a):
    g = 9.81
    theta = a / 180 * 3.14
    tmax = ((2 * v) * np.sin(theta)) / g
    timemat = tmax * np.linspace(0, 1, 40)

    x = (v * timemat) * np.cos(theta)
    y = ((v * timemat) * np.sin(theta)) - ((0.5 * g) * (timemat**2))
    df = pd.DataFrame({"x": x, "y": y})
    return df


class Kinematics(GradioDemoBase):
    def render(self) -> gr.blocks.Blocks | gr.interface.Interface:
        demo = gr.Blocks()

        with demo:
            gr.Markdown(
                r"Let's do some kinematics! Choose the speed and angle to see the trajectory. Remember that the range $R = v_0^2 \cdot \frac{\sin(2\theta)}{g}$"
            )

            with gr.Row():
                speed = gr.Slider(1, 30, 25, label="Speed")
                angle = gr.Slider(0, 90, 45, label="Angle")
            output = gr.LinePlot(
                x="x",
                y="y",
                overlay_point=True,
                tooltip=["x", "y"],
                x_lim=[0, 100],
                y_lim=[0, 60],
                width=350,
                height=300,
            )
            btn = gr.Button(value="Run")
            btn.click(plot, [speed, angle], output)

        return demo
