import os
from traceback import print_tb

import requests


def get_news(request):
    headers = {
        "Content-Type": "application/json"
    }
    try:
        res = requests.post(url=os.environ.get("API_NEWS_PATH"),headers=headers, json=request)
        return res
    except Exception as e:
        print(e)
