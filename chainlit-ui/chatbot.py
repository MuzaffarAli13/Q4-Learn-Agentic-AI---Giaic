# import chainlit as cl

# @cl.on_message
# async def main(message: cl.Message):
#     # Our custom logic goes here...
#     # Send a fake response back to the user
#     await cl.Message(
#         content=f"hello: {message.content}",
#     ).send()


import chainlit as cl
from chainlit_ui.main import myAgent  # ✅ yahan chatbots.main nahi, bas main agar same folder mein hai to

@cl.on_chat_start
async def chat_start():
    await cl.Message("Hello How I can Help you?").send()

@cl.on_message
async def main(message: cl.Message):
    user_input = message.content
    response = await myAgent(user_input)
    await cl.Message(content=f"{response}").send()
