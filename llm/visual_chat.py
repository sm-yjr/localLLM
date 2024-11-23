from .utils import create_chat_client, get_model_config
from .file_utils import process_uploaded_files

def visual_chat(inputs, history):
    """
    Process a single visual chat message and return the AI's response.

    Args:
        inputs (dict): Dictionary containing 'text' and 'files' keys
            Example: {"text": "这是什么图片？", "files": ["path/to/image1.jpg", "path/to/image2.jpg"]}
        history (list): The chat history, a list of dictionaries with 'role' and 'content' keys.

    Returns:
        str: The AI's response to the user's message.
    """
    user_message = inputs.get("text", "")
    uploaded_files = inputs.get("files", [])

    # 构建消息内容列表
    content = []
    
    # 如果有上传文件，添加图片
    if uploaded_files:
        # 处理上传的文件，转换为base64
        encoded_images = process_uploaded_files(uploaded_files)
        # 添加所有图片
        for img in encoded_images:
            content.append({
                "type": "image_url",
                "image_url": {"url": img}
            })
    
    # 无论是否有图片，都添加文本内容
    content.append({
        "type": "text",
        "text": user_message
    })

    client = create_chat_client()
    model_config = get_model_config("visual")

    # Append the user's message to the history
    history.append({"role": "user", "content": content})
    
    # Get AI response
    response = client.chat.completions.create(
        model=model_config["name"],
        messages=history,
        stream=True,
        extra_body=model_config["extra_body"],
        temperature=model_config["temperature"]
    )

    # Collect the AI's response
    ai_response = ""
    for chunk in response:
        content = chunk.choices[0].delta.content
        if content is not None:
            ai_response += content
            yield ai_response

    # Append the AI's response to the history
    history.append({"role": "assistant", "content": ai_response}) 