#!/usr/bin/python3

"""
Module defines a BaseModel class for managing objects with unique identifiers,
creation timestamps, and update timestamps. It also provides methods for saving
objects and converting them to dictionary representations.
"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """
    A class representing a base model with unique identifiers and timestamps.
    """

    def __init__(self, *args, **kwargs):

        """
        Initializes new instance of the BaseModel class with a unique id
        and creation/update timestamps.
        """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

        if kwargs:
            for i, j in kwargs.items():
                if i == "__class__":
                    continue
                if i == "created_at" or i == "updated_at":
                    setattr(self, i, datetime.strptime(j, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, i, j)

        models.storage.new(self)

    def save(self):
        """
        Updates the 'updated_at' attribute to the current date and time.
        """
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """
        Converts the instance attributes to a dictionary representation.

        Returns:
            dict: A dictionary containing the instance attributes.
        """
        instance_dict = self.__dict__.copy()
        instance_dict["__class__"] = self.__class__.__name__
        instance_dict["created_at"] = self.created_at.isoformat()
        instance_dict["updated_at"] = self.updated_at.isoformat()
        return instance_dict

    def __str__(self):
        """
        Returns a string representation of the instance.

        Returns:
            str: A string representation of the instance.
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
