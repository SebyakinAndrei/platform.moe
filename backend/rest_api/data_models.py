from pydantic import BaseModel, conint
from typing import List
from enum import Enum


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None


class SortBy(str, Enum):
    post_id = 'post_id'
    rating = 'rating'


class SearchBody(BaseModel):
    tags: List[str] = []
    sort_by: SortBy


class TimeSlice(str, Enum):
    day = 'day'
    week = 'week'
    month = 'month'
    year = 'year'


class ImageItem(BaseModel):
    image_id: conint(gt=0)
    height: conint(gt=100)
    width: conint(gt=100)


class ImageItemList(BaseModel):
    __root__: List[ImageItem]