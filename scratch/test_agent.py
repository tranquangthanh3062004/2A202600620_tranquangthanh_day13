import os
from dotenv import load_dotenv

# Enable debug logging for Langfuse
os.environ["LANGFUSE_DEBUG"] = "True"
load_dotenv(override=True)

from app.agent import LabAgent
from langfuse.decorators import langfuse_context

def main():
    print("Testing Agent directly...")
    agent = LabAgent()
    
    result = agent.run(
        user_id="test_user",
        feature="qa",
        session_id="s123",
        message="Hello World"
    )
    
    print(f"Agent result: {result.answer}")
    
    print("Flushing Langfuse...")
    langfuse_context.flush()
    print("Done!")

if __name__ == "__main__":
    main()
