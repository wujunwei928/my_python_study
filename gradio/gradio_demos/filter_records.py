import gradio as gr
import numpy as np

from .base import GradioDemoBase


def filter_records(records, gender):
    return records[records["gender"] == gender]


class FilterRecords(GradioDemoBase):
    def render(self) -> gr.blocks.Blocks | gr.interface.Interface:
        demo = gr.Interface(
            fn=filter_records,
            inputs=[
                gr.Dataframe(
                    headers=["name", "age", "gender"],
                    datatype=["str", "number", "str"],
                    value=[
                        ["Alice", 25, "F"],
                        ["Bob", 30, "M"],
                        ["Charlie", 35, "M"],
                        ["David", 40, "O"],
                        ["Eve", 45, "F"],
                    ],
                    row_count=5,
                    col_count=(3, "fixed"),
                ),
                gr.Dropdown(["M", "F", "O"]),
            ],
            outputs="dataframe",
            description="Enter gender as 'M', 'F', or 'O' for other.",
        )
        return demo
