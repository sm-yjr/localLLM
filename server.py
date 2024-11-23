import gradio as gr
from llm.visual_chat import visual_chat

gr.ChatInterface(visual_chat, 
                 title="AI聊天助手",
                 description="输入你的问题，AI将为你提供答案。",
                 type="messages",
                 theme="soft",
                 multimodal=True,
).launch()
