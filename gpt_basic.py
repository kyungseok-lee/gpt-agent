import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get OpenAI API key from environment variables
api_key = os.getenv('OPENAI_API_KEY')

# Validate API key
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in environment variables. Please check your .env file.")

# Initialize OpenAI client with API key
client = OpenAI(api_key=api_key)

try:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": "Hello!"}],
    )
    
    print(response.choices[0].message.content)
except Exception as e:
    print(f"Error occurred: {e}")