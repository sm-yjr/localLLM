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

def get_model_config(chat_type: str):
    """
    获取指定聊天类型的模型配置

    Args:
        chat_type (str): 聊天类型，'text' 或 'visual'

    Returns:
        dict: 模型配置信息
    """
    config = load_config()
    return config["models"].get(chat_type, {}) 