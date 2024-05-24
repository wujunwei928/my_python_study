import gradio as gr

from gradio_demos import HelloWorld, HelloBlocks, SentenceBuilder
from gradio_demos import DiffTexts, SepiaFilter, VideoIdentity
from gradio_demos import IterativeOutput, GenerateTone, FilterRecords
from gradio_demos import TransposeMatrix, TaxCalculator, Kinematics
from gradio_demos import StockForecast, TabbedInterface, Chatbot
from gradio_demos import StreamingChatbot, Layouts, Error, ChainedEvents
from gradio_demos import ChangeListener, DevTools, CrudDemo


demo_list = [
    # text 文本
    HelloWorld(),       # hello world demo
    HelloBlocks(),      # blocks demo
    SentenceBuilder(),  # 句子生成器
    DiffTexts(),        # 文本比较

    # media 多媒体
    SepiaFilter(),      # 棕褐色滤镜
    VideoIdentity(),    # 视频识别
    IterativeOutput(),  # 迭代输出
    GenerateTone(),     # 生成音调

    # tabular 表格
    FilterRecords(),    # 过滤记录
    TransposeMatrix(),  # 转置矩阵
    TaxCalculator(),    # 税收计算器
    Kinematics(),       # 运动学
    StockForecast(),    # 股票预测

    # other 其他
    TabbedInterface(),  # 标签界面
    Chatbot(),          # 聊天机器人
    StreamingChatbot(), # 流式聊天机器人
    Layouts(),          # 布局
    Error(),            # 错误
    ChainedEvents(),    # 链式事件
    ChangeListener(),   # 更改监听器

    # 自定义开发  研发工具集
    DevTools(),
    CrudDemo(),
]

tab_interface_list = []
tab_name_list = []
for demo in demo_list:
    tab_interface_list.append(demo.render())
    tab_name_list.append(demo.get_demo_name())

tabbed_demo = gr.TabbedInterface(
    interface_list=tab_interface_list,
    tab_names=tab_name_list,
    title="gradio playground 例子: https://www.gradio.app/playground")

if __name__ == "__main__":
    tabbed_demo.launch()
