import json
from openai import OpenAI

# 加载 config.json 文件
with open("config.json", "r") as config_file:
    config = json.load(config_file)

client = OpenAI(
    api_key=config["OPENAI_API_KEY"],
    base_url=config["OPENAI_BASE_URL"]
)

response = client.chat.completions.create(
    model="qwen-plus",
    messages=[{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": "Hello!"}],
    stream=True
)

for chunk in response:
    print(chunk.choices[0].delta.content, end="", flush=True)
print('\n')
