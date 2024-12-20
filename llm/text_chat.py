from .utils import create_chat_client, get_model_config

def text_chat(message, history):
    """
    Process a single chat message and return the AI's response.

    Args:
        message (str): The user's input message.
        history (list): The chat history, a list of dictionaries with 'role' and 'content' keys.

    Returns:
        str: The AI's response to the user's message.
    """
    client = create_chat_client()
    model_config = get_model_config("text")

    # Append the user's message to the history
    history.append({"role": "user", "content": message})

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

if __name__ == "__main__":
    # Initialize message history
    messages = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]
    
    print("欢迎使用AI聊天助手！输入 'quit' 或 'exit' 结束对话。")
    
    while True:
        # Get user input
        user_input = input("\n你: ").strip()
        
        # Check if the user wants to exit
        if user_input.lower() in ['quit', 'exit']:
            print("再见！")
            break
            
        # Get AI response as a stream
        print("\nAI助手: ", end="", flush=True)
        ai_response = ""
        for chunk in text_chat(user_input, messages):
            print(chunk[len(ai_response):], end="", flush=True)
            ai_response = chunk
        
        print() 