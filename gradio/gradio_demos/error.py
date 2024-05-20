import gradio as gr
import numpy as np

from .base import GradioDemoBase


def calculator(num1, operation, num2):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            raise gr.Error("Cannot divide by zero!")
        return num1 / num2
    

class Error(GradioDemoBase):
    def render(self) -> gr.blocks.Blocks | gr.interface.Interface:
        demo = gr.Interface(
            calculator,
            [
                "number", 
                gr.Radio(["add", "subtract", "multiply", "divide"]),
                "number"
            ],
            "number",
            examples=[
                [45, "add", 3],
                [3.14, "divide", 2],
                [144, "multiply", 2.5],
                [0, "subtract", 1.2],
            ],
            title="Toy Calculator",
            description="Here's a sample toy calculator. Allows you to calculate things like $2+2=4$",
        )
        return demo
