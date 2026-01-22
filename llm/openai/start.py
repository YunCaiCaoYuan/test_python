from openai import OpenAI
client = OpenAI(api_key="")

def simple_agent(query):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": query}]
    )
    return response.choices[0].message.content

simple_agent("你是谁")
