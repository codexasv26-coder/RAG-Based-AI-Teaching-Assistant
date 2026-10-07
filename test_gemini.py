import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("ERROR: GEMINI_API_KEY not found")
    exit()

print("API key found.")
print("Testing Gemini...")

client = genai.Client(api_key=api_key)

try:
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents="Reply with exactly: GEMINI_TEST_OK"
    )

    print("\nSUCCESS!")
    print(response.text)

except Exception as e:
    print("\nGEMINI ERROR:")
    print(e)