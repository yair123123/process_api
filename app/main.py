import time

from toolz import pipe

from app.flow import get_news_from_api, convert_news_model, convert_to_pd
from app.kafka_dir.flow import send_data

if __name__ == '__main__':
    i = 0
    while True:
        i += 1
        pd = pipe(
            get_news_from_api(i),
             lambda x: [convert_news_model(news) for news in x],
             convert_to_pd
             )
        send_data(df_data=pd)
        time.sleep(20)