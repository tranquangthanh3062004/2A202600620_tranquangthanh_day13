import os
import time
from langfuse import Langfuse
import logging

logging.basicConfig(level=logging.DEBUG)

def main():
    print("Testing Langfuse connection...")
    try:
        langfuse = Langfuse(
            public_key=os.getenv("LANGFUSE_PUBLIC_KEY"),
            secret_key=os.getenv("LANGFUSE_SECRET_KEY"),
            host=os.getenv("LANGFUSE_HOST")
        )
        print("Langfuse client initialized.")
        print(f"Public Key: {os.getenv('LANGFUSE_PUBLIC_KEY')}")
        print(f"Host: {os.getenv('LANGFUSE_HOST')}")
        
        if langfuse.auth_check():
            print("Successfully authenticated with Langfuse!")
        else:
            print("Failed to authenticate. Keys or URL might be wrong.")
        
    except Exception as e:
        print(f"Error connecting to Langfuse: {e}")

if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    main()
