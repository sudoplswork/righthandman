import os, sys, argparse
import types as pytypes
from config import SYSTEM_PROMPT
from dotenv import load_dotenv
from google import genai
from google.genai import types

from functions.call_function import call_function, available_functions


load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

def generate_content(messages, args):
    gemini_response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT,
            tools=[available_functions],
        ),
    )

    function_responses = []
    # Check if there are function calls before iterating
    if gemini_response.function_calls:
        for fc in gemini_response.function_calls:
            result = call_function(fc, args.verbose)
            if not result.parts or not result.parts[0].function_response:
                raise Exception("empty function call result")
            if args.verbose:
                print(f"-> {result.parts[0].function_response.response}")
            function_responses.append(result.parts[0])

    return gemini_response, function_responses



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
    print("Your right hand man says: ")
    try:
        i = 0
        while i < 20:
            ai_reply, tool_results = generate_content(messages, args)
            
            # Add the model's response (including function call decisions) to messages
            for candidate in ai_reply.candidates:
                messages.append(candidate.content)
            
            # If there are no function calls, we're done - print final response
            if not ai_reply.function_calls:
                print("Final response:")
                print(ai_reply.text)
                break
            
            # Otherwise, add the tool results and continue looping
            for part in tool_results:
                messages.append(types.Content(role="user", parts=[part]))
            
            i += 1
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"You forgot something bud, this might help: {e}")
        sys.exit(1)