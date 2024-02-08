#!/usr/bin/python3

"""
Module defines a BaseModel class for managing objects with unique identifiers,
creation timestamps, and update timestamps. It also provides methods for saving
objects and converting them to dictionary representations.
"""

import uuid
from datetime import datetime


class BaseModel:
    """
    A class representing a base model with unique identifiers and timestamps.
    """

    def __init__(self, *args, **kwargs):

        """
        Initializes new instance of the BaseModel class with a unique id
        and creation/update timestamps.
        """
        format_time = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for i, j in kwargs.items():
                if i == "__class__":
                    continue
                if i == "created_at" or i == "updated_at":
                    setattr(self, i, datetime.strptime(j, format_time))
                else:
                    setattr(self, i, j)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()

    def save(self):
        """
        Updates the 'updated_at' attribute to the current date and time.
        """
        self.updated_at = datetime.utcnow()

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


if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "My First Model"
    my_model.my_number = 89
    print(my_model)

    my_model.save()
    print(my_model)

    my_model_json = my_model.to_dict()
    print(my_model_json)

    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(
            my_model_json[key]), my_model_json[key]))
