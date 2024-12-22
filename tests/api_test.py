import os

from dotenv import load_dotenv

from app.api.news_api import get_news
from app.api.gruq_api import get_detail_from_news

load_dotenv(verbose=True)


def test_get_news():
    request = {
        "action": "getArticles",
        "keyword": "terror attack",
        "ignoreSourceGroupUri": "paywall/paywalled_sources",
        "articlesPage": 1,
        "articlesCount": 100,
        "articlesSortBy": "socialScore",
        "articlesSortByAsc": False,
        "dataType": [
            "news",
            "pr"
        ],
        "forceMaxDataTimeWindow": 31,
        "resultType": "articles",
        "apiKey": os.environ.get("API_NEWS_KEY")
    }
    res = get_news(request)
    print(res)
    res = res.json()
    assert res


def test_get_details_from_news():
    news = """A truck driver deliberately rammed into a crowded Christmas market in central Berlin, Germany, injuring dozens. Witnesses reported the driver accelerated toward the market, targeting the large crowd gathered for holiday festivities."""
    res = get_detail_from_news(news)
    print(res)
    assert res
