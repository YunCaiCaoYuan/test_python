#!/usr/bin/env python3
import os
import json
import requests
from dotenv import load_dotenv
from typing import List, Dict, Any

# 加载环境变量（.env 文件配置不变）
load_dotenv()

class DeepSeekAgent:
    def __init__(self):
        # 基础配置（从环境变量读取）
        self.api_key = os.getenv("DEEPSEEK_API_KEY")
        self.base_url = os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com/v1")
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        # 上下文记忆
        self.conversation_history: List[Dict[str, str]] = []
        # 可调用工具
        self.tools = {
            "calculator": self.calculator_tool,
            "weather": self.weather_tool
        }

    def calculator_tool(self, expression: str) -> str:
        """计算器工具：安全执行数学运算"""
        try:
            import ast
            # 安全解析表达式，避免恶意代码
            node = ast.parse(expression, mode='eval')
            # 仅允许数字和基础运算符
            allowed_nodes = (ast.Expression, ast.Num, ast.BinOp, ast.Add, ast.Sub, 
                            ast.Mult, ast.Div, ast.Mod, ast.Pow, ast.UnaryOp, ast.USub)
            for n in ast.walk(node):
                if not isinstance(n, allowed_nodes):
                    raise ValueError(f"不支持的运算：{type(n).__name__}")
            result = eval(compile(node, '<string>', 'eval'))
            return f"计算结果：{expression} = {result}"
        except Exception as e:
            return f"计算失败：{str(e)}"

    def weather_tool(self, city: str) -> str:
        """天气查询工具（示例）"""
        return f"{city} 当前天气：晴，温度 25℃，风力 2 级"

    def call_deepseek_api(self, prompt: str) -> str:
        """直接调用 DeepSeek API（OpenAI 兼容格式）"""
        # 构建 API 请求体
        payload = {
            "model": "deepseek-chat",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.1,
            "response_format": {"type": "json_object"},
            "max_tokens": 1024
        }

        try:
            # 发送 POST 请求
            response = requests.post(
                url=f"{self.base_url}/chat/completions",
                headers=self.headers,
                json=payload,
                timeout=30
            )
            response.raise_for_status()  # 抛出 HTTP 错误
            # 解析响应
            response_data = response.json()
            return response_data["choices"][0]["message"]["content"]
        except requests.exceptions.RequestException as e:
            return f"API 调用失败：{str(e)}"
        except KeyError as e:
            return f"响应解析失败：缺少字段 {e}"

    def think(self, user_input: str) -> Dict[str, Any]:
        """智能体思考逻辑：判断是否调用工具"""
        # 构造结构化提示词（强制 JSON 输出）
        prompt = f"""
        你的唯一任务是根据用户输入，输出严格的 JSON 格式结果，不要添加任何额外文字、解释或符号。
        JSON 格式要求：
        {{
            "need_tool": true 或 false,
            "tool_name": "calculator"、"weather" 或 "null",
            "tool_params": {{对应的参数键值对，如 {{\"expression\": \"1+1\"}} 或 {{\"city\": \"北京\"}}}},
            "answer": "不需要工具时的直接回答内容"
        }}
        
        用户输入：{user_input}
        """

        # 调用 API 获取思考结果
        api_result = self.call_deepseek_api(prompt)
        
        # 解析 JSON 结果
        try:
            return json.loads(api_result)
        except json.JSONDecodeError as e:
            return {
                "need_tool": False,
                "tool_name": "null",
                "tool_params": {},
                "answer": f"无法解析思考结果：{str(e)}，原始返回：{api_result[:100]}"
            }

    def run(self, user_input: str) -> str:
        """运行智能体主逻辑"""
        # 1. 智能体思考
        thought_result = self.think(user_input)
        
        # 2. 执行工具调用或直接回答
        if thought_result["need_tool"] and thought_result["tool_name"] in self.tools:
            tool_name = thought_result["tool_name"]
            tool_params = thought_result["tool_params"]
            try:
                # 调用工具（处理参数为空的情况）
                tool_result = self.tools[tool_name](**tool_params)
                answer = f"✅ 调用【{tool_name}】工具结果：\n{tool_result}"
            except Exception as e:
                answer = f"❌ 工具调用失败：{str(e)}"
        else:
            answer = thought_result.get("answer", "😯 暂无有效回答")
        
        # 3. 保存对话历史
        self.conversation_history.append({
            "user": user_input,
            "assistant": answer
        })
        
        return answer

# 测试智能体
if __name__ == "__main__":
    # 检查 API Key 是否配置
    if not os.getenv("DEEPSEEK_API_KEY"):
        print("⚠️  警告：未配置 DEEPSEEK_API_KEY，请在 .env 文件中添加")
        exit(1)
    
    agent = DeepSeekAgent()
    print("🚀 DeepSeek 智能体已启动（输入 'exit' 退出）")
    while True:
        user_input = input("\n你：")
        if user_input.lower() == "exit":
            print("智能体：再见！👋")
            break
        # 运行智能体并输出结果
        response = agent.run(user_input)
        print(f"智能体：{response}")
