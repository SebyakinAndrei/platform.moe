from pydantic import BaseModel, conint, ValidationError, validator
from typing import List, Optional
from enum import Enum


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None


class Status(str, Enum):
    error = 'error'
    ok = 'ok'


class BaseResponse(BaseModel):
    status: Status
    msg: str = ''


class SortBy(str, Enum):
    post_id = 'post_id'
    rating = 'rating'


class SearchBody(BaseModel):
    tags: List[str] = []
    sort_by: SortBy
    offset: int = 0
    posts_returned_first_time: conint(gt=0)


class TimeSlice(str, Enum):
    day = 'day'
    week = 'week'
    month = 'month'
    year = 'year'


class ImageItem(BaseModel):
    image_id: conint(gt=0)
    height: conint(gt=100)
    width: conint(gt=100)


class ArtistCard(BaseModel):
    preview_images: List[ImageItem]
    artist_tag: str
    artist_name: str


class TagInfo(BaseModel):
    name: str
    category: str
    num_posts: conint(gt=-1)


class ImageItemList(BaseModel):
    __root__: List[ImageItem]


test_img_lst = {[
    {
        'image_id': 1,
        'height': 845,
        'width': 300
    },
    {
        'image_id': 2,
        'height': 845,
        'width': 300
    }
]}

test_artist_card = {
    'preview_images': [
        {
            'image_id': 1,
            'height': 845,
            'width': 300
        },
        {
            'image_id': 2,
            'height': 845,
            'width': 300
        }
    ],
    'artist_tag': 'test_tag',
    'artist_name': 'Artist name'
}

test_ok_response = {'status':' ok', 'msg': 'all ok'}

test_followings = {}

test_tag_list = ['red_eyes red_dress', '1girl', 'blue_eyes']

test_tag_info_list = [
    {
        'name': '1girl',
        'category': 'general',
        'num_posts': 100000
    },
    {
        'name': 'blue_dress',
        'category': 'general',
        'num_posts': 20000
    },
    {
        'name': 'red_eyes',
        'category': 'general',
        'num_posts': 10000
    },
    {
        'name': 'apron',
        'category': 'general',
        'num_posts': 400000
    }
]