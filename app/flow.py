import os
import random
from dataclasses import asdict
from typing import Dict, List

import pandas as pd
from geopy import Nominatim
from app.api.gruq_api import get_detail_from_news
from app.api.news_api import get_news
from app.model_news import News

def get_location_info(city, country):
    return f"{city}, {country}" if city and country else (city if city else country)


def convert_address_to_points(address):
    geolocator = Nominatim(user_agent="geo_locator")
    location = geolocator.geocode(address)
    if location:
        return location.latitude, location.longitude
    return None


def convert_to_pd(news: List[News]):
    if news is None:
        return
    events_dicts = [asdict(event) for event in news if event]
    return pd.DataFrame(events_dicts)


def convert_news_model(news):
    try:
        res_dict = get_detail_from_news(news.get("body"))
        if not res_dict:
            return
        location = get_location_info(res_dict.get("city"), res_dict.get("country"))
        lat_lon = convert_address_to_points(location) if location else None
        res_dict["latitude"], res_dict["longitude"] = lat_lon if lat_lon else (None, None)
        res_dict["year"], res_dict["month"], res_dict["day"] = news.get("date", "0000-00-00").split("-")
        res_dict["summary"] = news.get("body")
        res_dict["eventid"] = random.randint(1000000, 9999999)
        return News(**res_dict)
    except Exception as e:
        print(e)
        return None

def get_news_from_api(page=1) -> List[Dict[str, str]]:
    request = {
        "action": "getArticles",
        "keyword": "terror attack",
        "ignoreSourceGroupUri": "paywall/paywalled_sources",
        "articlesPage": page,
        "articlesCount": 10,
        "articlesSortBy": "socialScore",
        "articlesSortByAsc": False,
        "dataType": ["news"],
        "forceMaxDataTimeWindow": 31,
        "resultType": "articles",
        "apiKey": os.environ.get("API_NEWS_KEY")
    }
    res = get_news(request).json()
    news = res.get("articles", {}).get("results", [])
    return news
