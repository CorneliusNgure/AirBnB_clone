#!/usr/bin/python3
"""Review class Module."""

from models.base_model import BaseModel


class Review(BaseModel):
    """Defines review.

    Attributes:
        place_id (str): Place id.
        user_id (str): User id.
        text (str): Review message.
    """

    place_id = ""
    user_id = ""
    text = ""
