#!/usr/bin/python3
"""Amenity class module"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Defines an Amenity

    Attributes:
        name(str): name of the aminity
    """

    name = ""
