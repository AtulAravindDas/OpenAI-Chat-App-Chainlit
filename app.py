import chainlit as cl
from openai import AsyncOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

MODEL = "gpt-4o-mini"  

gen_args = {
    "temperature": 0,
    "max_tokens": 900,
    "top_p": 1,
    "frequency_penalty": 0,
    "presence_penalty": 0,
    "stop": ["```"],
}

client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@cl.on_chat_start
async def on_start():
    await cl.Message(
        content="Hi, what can I do for you today?!",
        elements=[
            cl.Image(
                name="demo",
                display="inline",
                url="https://raw.githubusercontent.com/AtulAravindDas/OpenAI-Chat-App-Chainlit/main/Hi.gif",
            )
        ],
    ).send()

@cl.on_message
async def main(message: cl.Message):
    msg = await cl.Message(content="").send()

    
    stream = await client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": message.content}],
        stream=True,
        **gen_args,
    )

    async for chunk in stream:
        delta = chunk.choices[0].delta
        if delta and delta.content:
            await msg.stream_token(delta.content)

    await msg.update()
