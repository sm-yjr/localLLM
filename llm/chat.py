import json
from openai import OpenAI

def load_config():
    with open("config.json", "r") as config_file:
        return json.load(config_file)

def create_chat_client():
    config = load_config()
    return OpenAI(
        api_key=config["OPENAI_API_KEY"],
        base_url=config["OPENAI_BASE_URL"]
    )

def chat():
    client = create_chat_client()
    # 初始化消息历史
    messages = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]
    
    print("欢迎使用AI聊天助手！输入 'quit' 或 'exit' 结束对话。")
    
    while True:
        # 获取用户输入
        user_input = input("\n你: ").strip()
        
        # 检查是否退出
        if user_input.lower() in ['quit', 'exit']:
            print("再见！")
            break
            
        # 添加用户消息到历史记录
        messages.append({"role": "user", "content": user_input})
        
        # 获取AI响应
        print("\nAI助手: ", end="", flush=True)
        response = client.chat.completions.create(
            model="qwen-plus",
            messages=messages,
            stream=True,
            extra_body={"enable_search": True},
            temperature=0.8
        )
        
        # 收集完整的AI响应
        ai_response = ""
        for chunk in response:
            content = chunk.choices[0].delta.content
            if content is not None:
                print(content, end="", flush=True)
                ai_response += content
                
        # 添加AI响应到历史记录
        messages.append({"role": "assistant", "content": ai_response})
        print()  # 换行

if __name__ == "__main__":
    chat()
