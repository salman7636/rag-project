import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("❌ GOOGLE_API_KEY not found")
    exit()

print("✅ API key loaded")

llm = ChatGoogleGenerativeAI(
 model="gemini-3.6-flash",
    google_api_key=api_key,
    temperature=0.2
)

response = llm.invoke(
    "Say hello. Reply with exactly: Gemini is working!"
)

print("\n🤖 Gemini response:")
print(response.content)