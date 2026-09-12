from openai import OpenAI

from smart_ats.mock_responses import get_mock_analysis_response


def get_llm_response(
    input_prompt,
    config,
):
    """
    Returns an LLM response using the configured provider.

    Application configuration is loaded and validated
    before this function is called.
    """

    if config.llm_mode == "mock":
        return get_mock_analysis_response()

    client = OpenAI(
        api_key=config.deepseek_api_key,
        base_url="https://api.deepseek.com",
    )

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {
                "role": "user",
                "content": input_prompt,
            }
        ],
    )

    return response.choices[0].message.content
