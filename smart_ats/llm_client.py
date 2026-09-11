import os

from dotenv import load_dotenv
from openai import OpenAI
from smart_ats.mock_responses import get_mock_analysis_response

load_dotenv()

api_key = os.getenv("DEEPSEEK_API_KEY")
llm_mode = os.getenv("LLM_MODE", "mock")

client = OpenAI(
    api_key=api_key,
    base_url="https://api.deepseek.com"
)


def get_llm_response(input_prompt):
    """
    Returns an LLM response using either mock mode or DeepSeek.
    """

    if llm_mode == "mock":
        return get_mock_analysis_response()

    if llm_mode != "deepseek":
        return (
            f"Error: Unsupported LLM_MODE '{llm_mode}'. "
            "Use 'mock' or 'deepseek'."
        )

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
        return (
            "An error occurred while contacting "
            f"the DeepSeek API: {e}"
        )