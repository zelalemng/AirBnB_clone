#!/usr/bin/python3
'''class inherent of Base Model'''
from models.base_model import BaseModel

class Place(BaseModel):
    '''class place'''
    city_id = ""
    user_id = ""
    name = ""
    description = 0
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """initializes place"""
        super().__init__(*args, **kwargs)
