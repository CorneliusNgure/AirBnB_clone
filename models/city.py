#!/usr/bin/python3
"""City class module"""

from models.base_module import BaseModel


class City(BaseModel):
    """
    Defines a city

    Attributes:
        state_id(str): the id of the state
        name(str): name of the city
    """

    state_id = ""
    name = ""
