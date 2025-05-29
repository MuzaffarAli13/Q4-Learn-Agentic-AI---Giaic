import os 
from agents import Agent, Runner,OpenAIChatCompletionsModel, AsyncOpenAI,set_tracing_disabled 
from dotenv import load_dotenv 

def agent():
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
            input=f"""what will be the output of the following code? 
            abc = 123
            let abc = 456
            console.log(abc)
            """, 
        ) 
    print("-"* 20)
    print("Response from the agent:")
    print(response.final_output) 
    print("-"* 20)
    
if __name__ == "__main__":
    agent() 
    # To run the agent asynchronously, you can use the following code:
    # import asyncio
    # asyncio.run(agent())