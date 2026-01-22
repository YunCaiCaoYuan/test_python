#!/usr/bin/env python3
from openai import OpenAI
import os

# 设置DeepSeek API
client = OpenAI(
    api_key="sk-5d8f7f71183b4b0dabba36e2bf0702bb",
    base_url="https://api.deepseek.com"
)

def deepseek_chat(messages):
    response = client.chat.completions.create(
        model="deepseek-chat",  # 或 "deepseek-coder"
        messages=messages,
        temperature=0.7,
        max_tokens=2000
    )
    return response.choices[0].message.content

# 使用示例
messages = [
    {"role": "system", "content": "你是一个有用的助手"},
    {"role": "user", "content": "你好，请介绍一下自己"}
]
response = deepseek_chat(messages)
print(response)
