import os
import requests
from dotenv import load_dotenv

load_dotenv(override=True)

PUBLIC_KEY = os.getenv("LANGFUSE_PUBLIC_KEY")
SECRET_KEY = os.getenv("LANGFUSE_SECRET_KEY")
HOST = os.getenv("LANGFUSE_HOST", "https://cloud.langfuse.com").rstrip("/")

def check_traces():
    url = f"{HOST}/api/public/traces"
    print(f"Checking traces at: {url}")
    
    try:
        response = requests.get(
            url,
            auth=(PUBLIC_KEY, SECRET_KEY),
            params={"limit": 100} # Get the 100 most recent traces
        )
        
        if response.status_code == 200:
            data = response.json()
            traces = data.get("data", [])
            
            if not traces:
                print("No traces found in this Langfuse project. Are you sure you are using the correct keys?")
                return
                
            print(f"SUCCESS! Found {data.get('meta', {}).get('totalItemCount', len(traces))} total traces in this project.")
            print("\nHere are the 5 most recent traces:")
            for i, trace in enumerate(traces, 1):
                name = trace.get("name")
                id = trace.get("id")
                latency = trace.get("latency")
                timestamp = trace.get("timestamp")
                print(f"  {i}. [Name: {name}] - [ID: {id}] - [Latency: {latency}s] - [Time: {timestamp}]")
        else:
            print(f"Failed to fetch traces. Status code: {response.status_code}")
            print(f"Error details: {response.text}")
            
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    check_traces()
