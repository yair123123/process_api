from dataclasses import dataclass


@dataclass
class News:
    eventid: str
    year: str
    month: str
    day: str
    city: str
    country: str
    region: str
    group_name:str
    group_name2:str
    attacktype1_txt: str
    target_type: str
    target1: str
    latitude: float
    longitude: float
    num_terrorists: int
    num_spread: int
    num_killed: int
    summary: str

