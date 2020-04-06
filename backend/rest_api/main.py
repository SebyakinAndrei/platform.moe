from fastapi import FastAPI
from data_models import *

app = FastAPI()


@app.post('/search/')
async def search(query: SearchBody, response_model=List[ImageItem]):
    return {[
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


@app.get('/popular/{slice}')
async def get_popular(slice: TimeSlice, response_model=List[ImageItem]):
    return {[
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



