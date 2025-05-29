# Build a Gemini AI Agent Using UV

This repository guides you through building an intelligent AI agent powered by Google Geminî via the `openai-agents` package and UV tooling.

## Objective

- Initialize a UV Python project (as in Task 1).
- Use Google's Gemini API through the `openai-agents` client.
- Create a simple agent that responds to basic questions.

## Prerequisites

- Python 3.8+
- UV CLI installed (see Task 1 instructions)
- A Gemini API key from [AI Studio](https://aistudio.google.com/app/apikey)

## 1. Initialize the UV Project

Follow the steps from Task 1 to create and activate a new UV project.

```bash
uv init my-gemini-agent
cd my-gemini-agent
```

## 2. Install Dependencies

Install the required Python packages:

```bash
uv add openai-agents
uv add python-dotenv
```

- **`openai-agents`**: Structured framework for building AI agents (compatible with Gemini).
- **`python-dotenv`**: Loads environment variables from a `.env` file.

## 3. Configure Environment Variables

Create a `.env` file in the project root and add your Gemini API key:

```ini
GEMINI_API_KEY=your_api_key_here
```

## 4. Create the Agent Script

Create a new file (e.g., `main.py`) with the following content:

```python
from dotenv import load_dotenv
from agents import (
    Agent,
    Runner,
    OpenAIChatCompletionsModel,
    AsyncOpenAI,
    set_tracing_disabled,
)
import os

# Load .env
load_dotenv()
# Disable internal tracing for cleaner output
set_tracing_disabled(True)

# Configure Gemini provider
provider = AsyncOpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# Choose the Gemini model
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash-exp",
    openai_client=provider,
)

# Define the agent
assistant = Agent(
    name="Assistant",
    instructions="You are a helpful assistant that solves basic math problems.",
    model=model,
)

# Run the agent synchronously
response = Runner.run_sync(
    starting_agent=assistant,
    input="What is 5 + 10?",
)

print(response.final_output)
```  

## 5. Run the Script

Execute your script with UV:

```bash
uv run main.py
```

## 6. Code Explanation

- **`dotenv.load_dotenv()`**: Loads environment variables from `.env`.
- **`AsyncOpenAI`**: Connects to the Gemini API endpoint with your key.
- **`OpenAIChatCompletionsModel`**: Wraps the Gemini model (`gemini-2.0-flash-exp`).
- **`Agent`**: Defines a conversational agent with given name and behavior.
- **`Runner.run_sync()`**: Runs the agent synchronously and returns the final output.

Feel free to customize the instructions, model choice, or input prompts to explore more advanced use cases!

___

## 🌐 Connect With Me

Let’s connect and grow together on these platforms:

- [🎥 YouTube](https://www.youtube.com/@muzaffaritacademy)
- [👍 Facebook](https://www.facebook.com/profile.php?id=100093557110026)
- [🔗 LinkedIn](https://www.linkedin.com/in/muzaffar-ali-0b3939315/)

**Let’s keep learning, growing, and pushing our tech journeys to the next level!** 🚀

---

> **“Knowledge shared is knowledge multiplied.”** ✨

