from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from data_models import *

app = FastAPI()


@app.post('/search')
async def search(query: SearchBody, response_model=List[ImageItem]):
    return test_img_lst


@app.get('/popular/{slice}')
async def get_popular(slice: TimeSlice, response_model=List[ImageItem]):
    return test_img_lst


@app.get('/get_updates')
async def get_updates(offset: int, posts_returned_first_time: int = None, response_model=List[ImageItem]):
    return test_img_lst


@app.get('/favorites')
async def get_favorites(offset: int, posts_returned_first_time: int = None, response_model=List[ImageItem]):
    return test_img_lst


@app.get('/get_recommended')
async def get_recommended(response_model=List[ArtistCard]):
    return [test_artist_card]*5


@app.post('/follow')
async def follow(query: str, response_model=BaseResponse):
    return test_ok_response


@app.get('/followings')
async def get_followings(response_model=List[str]):
    return test_tag_list


@app.post('/add_to_favorites')
async def add_to_favorites(image_ids: List[int], response_model=BaseResponse):
    return test_ok_response


@app.post('/remove_from_favorites')
async def remove_from_favorites(image_ids: List[int], response_model=BaseResponse):
    return test_ok_response


@app.get('/tags')
async def get_tags(response_model=List[TagInfo]):
    return test_tag_info_list


# https://dropbox.tech/infrastructure/retrieving-thumbnails
@app.get('/thumbnails')
async def get_thumbnails(batch_size: int, response_model=str, response_class=PlainTextResponse):
    # Makes n async requests with aiohttp to seaweedfs server, then compose it to response
    return \
    """<image_id>:<data_uri>
    1844:data:image/jpeg;base64,4AAQ4BQY5FBAYmI4B...
    44445:data:image/jpeg;base64,I8FWC3EAj+4K846AF...
    """