# AI Agent Creation with OpenRouter and `uv`

This project demonstrates how to build a basic AI Agent using Python, [`uv`](https://github.com/astral-sh/uv), and [OpenRouter](https://openrouter.ai). OpenRouter provides unified access to various AI models from providers like OpenAI, Google, and Anthropic using a single API.

## 🌐 What is OpenRouter?

OpenRouter is like a meta-service that aggregates multiple language models and makes them accessible through one API. It simplifies experimentation and integration by supporting the OpenAI SDK format.

### 🔍 Why Use OpenRouter?

- Access multiple models with one API key
- Try free versions of popular models
- Compare behavior of different LLMs
- Works with OpenAI-compatible libraries

---

## ⚙️ Setup Instructions

### 1. Initialize a `uv` Project

You should have already initialized a `uv` project. If not, refer to the instructions in Task 1 or run:

```bash
uv venv
```

### 2. Install Required Dependencies

Install the needed packages using `uv`:

```bash
uv add openai-agents
uv add dotenv
```

### 3. Create a `.env` File

Add your OpenRouter API key in the `.env` file:

```env
OPENROUTER_API_KEY=your_api_key_here
```

You can get your API key from [https://openrouter.ai/keys](https://openrouter.ai/keys)

---

## 🧠 Example Code

You can use the following example in your `main.py` or another Python file:

```python
import os
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, set_tracing_disabled
from dotenv import load_dotenv

load_dotenv()
set_tracing_disabled(True)

provider = AsyncOpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

model = OpenAIChatCompletionsModel(
    model="google/gemini-2.0-flash-exp:free",
    openai_client=provider,
)

Agent1 = Agent(
    name="Assistant",
    instructions="You are a helpful assistant.",
    model=model
)

response = Runner.run_sync(
    starting_agent=Agent1,
    input="What is 5 % 5?",
)

print(response.final_output)
```

---

## 📌 Notes

- Make sure your `.env` file is not committed to version control.
- You can change the model in the `OpenAIChatCompletionsModel` by referencing other models available on OpenRouter.

---

## 📄 License

This project is for educational purposes only. Use at your own discretion.
