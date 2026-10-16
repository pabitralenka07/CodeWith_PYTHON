import os
from google import genai

# Fetch the API key from environment variables or prompt the user
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    api_key = input("Enter your Gemini API Key: ").strip()

client = genai.Client(api_key=api_key)

while True:
    question = input("You: ")

    if question.lower().strip() == "exit":
        print("Goodbye!")
        break

    try:
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=question
        )

        print("Gemini:", response.text)

    except Exception as e:
        print("Error:", e)
