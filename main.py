import os, sys, argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types


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
        help="Enable verbose output for debugging or detailed logs."
    )
    args = parser.parse_args()

    user_prompt = args.prompt
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]


    parser = argparse.ArgumentParser(
        description="Input what you need AI assistance with. Strings only rn"
    )
    

    print("Your right hand man says: ")
    gemini_response = client.models.generate_content(model = "gemini-2.0-flash-001", contents = messages)
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
        print("You forgot the query bud.")
        sys.exit(1)