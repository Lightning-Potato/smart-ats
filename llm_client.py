import os

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

api_key = os.getenv("DEEPSEEK_API_KEY")

client = OpenAI(
    api_key=api_key,
    base_url="https://api.deepseek.com"
)


def get_llm_response(input_prompt):
    """
    Sends a prompt to the DeepSeek model and returns the response.
    """
    if not api_key:
        return "Error: DeepSeek API key is not configured."

    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {
                    "role": "user",
                    "content": input_prompt
                }
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"An error occurred while contacting the DeepSeek API: {e}"