import random

import gradio as gr

from .base import GradioDemoBase
from models import user_crud


def create_user_interface(name, age):
    return user_crud.create_user(name, age)


def read_users_interface():
    users = user_crud.read_users()
    return '\n'.join([f"ID: {user[0]}, Name: {user[1]}, Age: {user[2]}" for user in users])


def update_user_interface(user_id, name, age):
    return user_crud.update_user(user_id, name, age)


def delete_user_interface(user_id):
    return user_crud.delete_user(user_id)


class CrudDemo(GradioDemoBase):
    def render(self) -> gr.blocks.Blocks | gr.interface.Interface:
        with gr.Blocks() as demo:
            gr.Markdown("## SQL ORM 增删改查")

            with gr.Tab("Create"):
                name = gr.Textbox(label="Name")
                age = gr.Number(label="Age")
                create_btn = gr.Button("Create")
                create_output = gr.Textbox()
                create_btn.click(create_user_interface, inputs=[name, age], outputs=create_output)

            with gr.Tab("Read"):
                read_btn = gr.Button("Read All Users")
                read_output = gr.Textbox()
                read_btn.click(read_users_interface, outputs=read_output)

            with gr.Tab("Update"):
                user_id = gr.Number(label="User ID")
                name = gr.Textbox(label="Name")
                age = gr.Number(label="Age")
                update_btn = gr.Button("Update")
                update_output = gr.Textbox()
                update_btn.click(update_user_interface, inputs=[user_id, name, age], outputs=update_output)

            with gr.Tab("Delete"):
                user_id = gr.Number(label="User ID")
                delete_btn = gr.Button("Delete")
                delete_output = gr.Textbox()
                delete_btn.click(delete_user_interface, inputs=user_id, outputs=delete_output)

        return demo
