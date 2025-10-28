import os, sys, argparse
import types as pytypes
from config import SYSTEM_PROMPT
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.run_python_file import schema_run_python_file
from functions.write_file import schema_write_file
from functions.call_function import call_function


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
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file
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
    

    # Seer stone'd sue me 
    function_responses = []
    for function_call_part in gemini_response.function_calls:
        function_call_result = call_function(function_call_part, args.verbose)

        # sanity check
        if (
            not function_call_result.parts
            or not function_call_result.parts[0].function_response
        ):
            raise Exception("empty function call result")

        # printing if verbose
        if args.verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")

        function_responses.append(function_call_result.parts[0])

    if not function_responses:
        raise Exception("no function responses generated, exiting.")
        # --- print final results ---
        
    if not function_responses:
        # model produced text only
        print(gemini_response.text)
        return

    # model invoked one or more tools -> print each result
    for part in function_responses:
        fr = part.function_response          # FunctionResponse object
        payload = getattr(fr, "response", {})  # dict like {"result": "..."}
        if args.verbose:
            print(f"Tool payload: {payload}")

        if not isinstance(payload, dict) or not payload.get("result"):
            raise ValueError(f"Fatal Error: tool output missing or empty result (payload={payload})")

        print(payload["result"])





if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"You forgot something bud, this might help: {e}")
        sys.exit(1)