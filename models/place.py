#!/usr/bin/python3
"""Defines place class"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Defines a place

    Attributes:
        city_id(str): City id
        user_id(str): User id
        name(str): name of a place
        description(str): Description of the place
        number_rooms(int): # of rooms
        number_bathrooms(int): # of bathrooms
        max_guest(int): maximum no. of guests
        price_by_night(int): price at night
        latitude(float): lattitude of the place
        longitude(float): longitude of the place
        amenity_ids(str): Amenity id list
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
