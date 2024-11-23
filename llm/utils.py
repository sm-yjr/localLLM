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