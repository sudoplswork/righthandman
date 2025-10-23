import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
user_prompt = sys.argv[1]
messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]

def main():
    print("Your right hand man says: ")
    if len(sys.argv) < 2 or not sys.argv[1]:
        print("You forgot the question, I need a command line argument to search with.")
        sys.exit(1)
    gemini_response = client.models.generate_content(model = "gemini-2.0-flash-001", contents = messages)
    print(gemini_response.text)
    print(f"Prompt tokens: {gemini_response.usage_metadata.prompt_token_count}\nResponse tokens: {gemini_response.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()
