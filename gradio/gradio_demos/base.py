import inspect
import os
from abc import ABC, abstractmethod

import gradio as gr


class GradioDemoBase(ABC):

    def get_demo_name(self) -> str:
        # 获取文件的路径名 ps: __file__ 获取的不准, 返回的始终是父类的路径, 不会根据子类自动判断
        class_file_path = inspect.getfile(self.__class__)
        class_file_name_with_ext = os.path.basename(class_file_path)
        class_file_name, _ = os.path.splitext(class_file_name_with_ext)
        return " ".join([x.title() for x in class_file_name.split("_")])

    @abstractmethod
    def render(self) -> gr.blocks.Blocks | gr.interface.Interface:
        pass
