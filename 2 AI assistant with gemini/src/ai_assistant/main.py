from dotenv import load_dotenv
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, set_tracing_disabled
import os

def agent():
    load_dotenv()
    set_tracing_disabled(True)
    
    provider = AsyncOpenAI(
        api_key=os.getenv("GEMINI_API_KEY"),
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )
    
    model = OpenAIChatCompletionsModel(
        model="gemini-2.0-flash-exp",
        openai_client=provider,
    )
    
    Agent1 = Agent(
        name="Assistant",
        instructions="You are a helpful assistant that solves basic math problems.",
        model=model
    )
    
    
    response = Runner.run_sync(
        starting_agent=Agent1,
        input= "Hello , Can you help me ?",
    )
    print("--" * 20)
    print(response.final_output)
    print("Agent finished successfully!")
    print("--" * 20)
    
if __name__ == "__main__":
    agent()
