#!/usr/bin/python3
"""
Module for handling serialization and deserialization processes.
"""

import json
import os
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """
    A class for managing object storage in JSON format.
    """
    
    __file_path = "file.json"
    __objects = {}

    def new(self, obj):
        """
        Adds a new object to the storage.
        """
        obj_cls_name = obj.__class__.__name__
        key = "{}.{}".format(obj_cls_name, obj.id)
        FileStorage.__objects[key] = obj

    def all(self):
        """
        Returns all objects in the storage.
        """
        return FileStorage.__objects

    def save(self):
        """
        Saves objects to a JSON file.
        """
        all_objects = FileStorage.__objects
        obj_dict = {}
        for obj in all_objects.keys():
            obj_dict[obj] = all_objects[obj].to_dict()
        
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """
        Reloads objects from a JSON file.
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                try:
                    obj_dict = json.load(f)
                    for key, values in obj_dict.items():
                        class_name, obj_id = key.split(".")
                        cls = eval(class_name)
                        new_instance = cls(**values)
                        FileStorage.__objects[key] = new_instance
                except Exception:
                    pass
