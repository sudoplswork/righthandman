import os, sys, argparse
from config import SYSTEM_PROMPT
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_files_info import schema_get_files_info

load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)



def main():

    parser = argparse.ArgumentParser(
        description="Input what you need AI assistance with. Strings only rn"
    )

    parser.add_argument(
        "prompt",
        help="The search term or question to input."
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose output for debugging or detailed logs.",
    )
    
    args = parser.parse_args()

    user_prompt = args.prompt
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        ]
    )

    print("Your right hand man says: ")
    gemini_response = client.models.generate_content(
        model = "gemini-2.0-flash-001", 
        contents = messages,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT,
            tools=[available_functions]
            )
        )
    

    
    func_calls = getattr(gemini_response, "function_calls", None)
    if func_calls:
        for func in func_calls:
            print(f"Calling function: {func.name}({func.args})")
    else:
        print(gemini_response.text)


    if args.verbose:
        print(
            f"User prompt: {user_prompt}\n"
            f"Prompt tokens: {gemini_response.usage_metadata.prompt_token_count}\n"
            f"Response tokens: {gemini_response.usage_metadata.candidates_token_count}"
            )


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"You forgot something bud, this might help: {e}")
        sys.exit(1)