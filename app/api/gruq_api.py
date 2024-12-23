import os

from dotenv import load_dotenv
from groq import Groq
load_dotenv(verbose=True)

import json


def get_detail_from_news(news):
    client = Groq(
        api_key=os.environ.get("API_GRUQ_KEY"),
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"""
                Is this a historical terrorist attack or a contemporary one? 
                If the text is not related to terrorism or cannot be classified, return `null`.
                If the text is related to a terrorist attack, return the answer in JSON format with the following structure:
                {{
                    "city": str or None,
                    "country": str or None,
                    "region": str or None,
                    "group_name": str or None, #name of group that performed the attack
                    "group_name2": str or None,#name of group2 that performed the attack
                    "attacktype1_txt": str or None,
                    "target_type": str or None,
                    "target1": str or None,
                    "num_terrorists": int or None,
                    "num_spread": int or None,
                    "num_killed": int or None,
                }}
                If any field is unknown or missing, return None for that field.
                Important: No text, just JSON or `null`.
                ONLY JSON I wont to convert it to dict in python
                You must return all fields even if they are not present.

                Text: {news}
                """
            }
        ],
        model="llama3-8b-8192"
    )

    response_text = chat_completion.choices[0].message.content.strip()

    if response_text == "null":
        return None
    try:
        return json.loads(response_text)
    except json.JSONDecodeError:
        print("Error: Invalid JSON format returned.")
        return None
