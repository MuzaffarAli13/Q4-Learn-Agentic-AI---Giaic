
# 📚 Day 2: Exploring Chainlit with UV

## 📌 Objective:
Today, we explored Python's AI framework **Chainlit**, set it up using `uv`, created a simple chatbot, and learned how to run it.

---

## 📖 Steps:

### ✅ 1️⃣ Project Setup

First, we created a project folder and set up a virtual environment using `uv`:

```bash
uv run --package .
```

---

### ✅ 2️⃣ Install Chainlit

Then, we installed Chainlit into our project:

```bash
uv add chainlit
```

---

### ✅ 3️⃣ Wrote the Code

Next, we created a `src` folder and inside it, a file named:

```
chatbot.py
```

And wrote the following code:

```python
import chainlit as cl

@cl.on_message
async def main(message: cl.Message):
    # Our custom chatbot logic goes here
    await cl.Message(
        content=f"hello: {message.content}",
    ).send()
```

---

### ✅ 4️⃣ Run the Chatbot

Finally, we ran the chatbot using:

```bash
uv run chainlit run src/chatbot.py -w
```

**Note:**  
The `-w` flag enables **watch mode**, which automatically reloads the app when you make changes to the file.

---

## 🎉 Result:

Whenever a user sends a message, our chatbot responds with the same message prefixed by **"hello: "**.

Example:

**User:** Hi  
**Bot:** hello: Hi  

---

## 📦 Summary:

- Set up a project with `uv`
- Installed the Chainlit package
- Created a simple chatbot
- Learned how to run and test the chatbot

---

## 🚀 Next Steps:

- Add more features to the chatbot
- Ask for the user’s name, take AI-based responses, or build a mini tool

---

✅ **End of Day 2**
