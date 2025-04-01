import datetime
import random
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get GitHub token from .env file
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

def main():
    if not GITHUB_TOKEN:
        print("Error: GitHub Token not found in .env file")
        return
    
    results = {
        "timestamp": datetime.datetime.now().isoformat(),
        "random_number": random.randint(1, 100),
        "status": "SUCCESS"
    }
    print("\n".join(f"{k}: {v}" for k, v in results.items()))

if __name__ == "__main__":
    main()
