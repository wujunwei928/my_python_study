import gradio as gr

from .base import GradioDemoBase


def sentence_builder(quantity, animal, countries, place, activity_list, morning):
    return (f'The {quantity} {animal}s from {" and ".join(countries)} went to the '
            f'{place} where they {" and ".join(activity_list)} until the '
            f'{"morning" if morning else "night"}')


class SentenceBuilder(GradioDemoBase):
    @staticmethod
    def greet(name: str):
        return f"Hello {name}!"

    def render(self) -> gr.blocks.Blocks | gr.interface.Interface:
        demo = gr.Interface(
            sentence_builder,
            inputs=[
                # 滑块
                gr.Slider(2, 20, value=4, label="Count",
                          info="Choose between 2 and 20"),
                # 单选下拉框
                gr.Dropdown(
                    choices=["cat", "dog", "bird"],
                    label="Animal",
                    info="Will add more animals later!"
                ),
                # 复选框
                gr.CheckboxGroup(
                    ["USA", "Japan", "Pakistan"],
                    label="Countries",
                    info="Where are they from?"),
                # 单选按钮
                gr.Radio(
                    ["park", "zoo", "road"],
                    label="Location",
                    info="Where did they go?"),
                # 多选下拉框
                gr.Dropdown(
                    ["ran", "swam", "ate", "slept"],
                    value=["swam", "slept"],
                    multiselect=True,
                    label="Activity",
                    info=("Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
                          "Sed auctor, nisl eget ultricies aliquam, nunc nisl aliquet "
                          "nunc, eget aliquam nisl nunc vel nisl.")
                ),
                # 复选框
                gr.Checkbox(label="Morning", info="Did they do it in the morning?"),
            ],
            outputs="text",
            examples=[
                [2, "cat", ["Japan", "Pakistan"], "park", ["ate", "swam"], True],
                [4, "dog", ["Japan"], "zoo", ["ate", "swam"], False],
                [10, "bird", ["USA", "Pakistan"], "road", ["ran"], False],
                [8, "cat", ["Pakistan"], "zoo", ["ate"], True],
            ]
        )

        return demo
