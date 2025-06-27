import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generera_coachtips(fråga: str) -> str:
    prompt = f"Du är en empatisk AI-livscoach. Använd max 60 ord. Fråga: {fråga}"

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=100
    )

    return response.choices[0].message.content.strip()