#!/usr/python3

import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def test_init(self):
        instance = BaseModel()

        self.assertIsNotNone(instance.id)
        self.assertIsNotNone(instance.date_created)
        self.assertIsNotNone(instance.date_updated)

    def test_save(self):
        instance = BaseModel()

        prev_date_updated = instance.date_updated
        current_date_updated = instance.save()

        self.assertNotEqual(prev_date_updated, current_date_updated)

    def test_to_dict(self):
        instance = BaseModel()

        instance_dict = instance.to_dict()

        self.assertIsInstance(instance_dict, dict)

        self.assertEqual(instance_dict["__class__"], "BaseModel")
        self.assertEqual(instance_dict["id"], instance.id)
        self.assertEqual(instance_dict["date_created"], instance.date_created.isoformat())
        self.assertEqual(instance_dict["date_updated"], instance.date_updated.isoformat())

    def test_str(self):
        instance = BaseModel()

        self.assertTrue(str(instance).startswith("[BaseModel]"))
        self.assertIn(instance.id, str(instance))
        self.assertIn(str(instance.__dict__), str(instance))

if __name__ == "__main__":
    unittest.main()
