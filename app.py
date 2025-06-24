import chainlit as cl

@cl.on_message
async def main(message: cl.Message):
    await cl.Message(content="Hi! This is a placeholder chatbot.").send()