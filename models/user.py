#!/usr/bin/python3

"""Module containing the User class"""

from models.base_model import BaseModel


class User(BaseModel):
    """Class containing user information"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
