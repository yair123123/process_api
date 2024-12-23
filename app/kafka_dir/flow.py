import os
from typing import List, Callable
import toolz as t
from dotenv import load_dotenv
from pandas import DataFrame

from app.kafka_dir.producers import publisher

load_dotenv(verbose=True)

def produce_chunks(data: DataFrame, produce: Callable, chunks_size: int = 100):
    for i in range(0,len(data), chunks_size):
        produce(data.iloc[i:i+chunks_size])

def send_data(df_data):
    produce_chunks(df_data,publisher("TOPIC","process_data"))

