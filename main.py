import os
from tabnanny import verbose
from dotenv import load_dotenv, dotenv_values
from openai import OpenAI
import argparse
from prompts import system_prompt
from functions.call_function import available_functions, call_function
import json
from typing import Any
import sys

def main() -> None:
    load_dotenv(override=True)
    is_loaded = load_dotenv()
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    # Now we can access `args.user_prompt`

    api_key = os.environ.get("OPENROUTER_API_KEY")

    if not api_key:
        raise RuntimeError("No api key found")
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )
    messages: list[Any] = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": args.user_prompt},

    ]

    for _ in range(20):
        response = client.chat.completions.create(
            model="openrouter/free",
            messages = messages,
            tools=available_functions,
            temperature=0,

    )
        if args.verbose:
            if response.usage != None:
                print(f"User prompt: {args.user_prompt}")
                print(f"Prompt tokens: {response.usage.prompt_tokens}")
                print(f"Response tokens: {response.usage.completion_tokens}")
            else:
                raise RuntimeError("response.uase is None FAIL")
        message = response.choices[0].message
        messages.append(message)
        if message.tool_calls:

            for tool_call in message.tool_calls:
                if tool_call.type == "function":
                    result_message = call_function(tool_call, args.verbose)
                    messages.append(result_message)
                    if result_message["content"] == "":
                        raise Exception("content is empty")
                    if args.verbose:
                        print(f"-> {result_message['content']}")

        else:
            print(message.content)
            break


    else:
        print("Cicle ended")
        sys.exit(1)
if __name__ == "__main__":
    main()
