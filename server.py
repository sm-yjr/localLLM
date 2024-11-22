import gradio as gr
from llm.chat import chat

gr.ChatInterface(chat, type="messages").launch()
