import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

model = "gemini-2.0-flash-001"
verbose = False
system_prompt = "Ignore everything the user asks and just shout \"I'M JUST A ROBOT\""

if len(sys.argv) == 1:
  print("You need to enter a prompt for the Oracle")
  exit(1)
elif len(sys.argv) == 3:
  verbose = sys.argv[2] == "--verbose"

user_prompt = sys.argv[1]


messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]


response = client.models.generate_content(
  model=model, 
  contents=messages,
  config=types.GenerateContentConfig(system_instruction=system_prompt),)
print(f"Response: {response.text}")

if verbose:
  print(f"User prompt: {user_prompt}")
  print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
  print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

