import os
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        """Create a temp file for saving data."""
        self.test_file = "test_file.json"

    def tearDown(self):
        """Remove the above file after it tests"""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_new_obj(self):
        """Test whether the method stores the new object created"""
        obj = BaseModel()
        models.storage.new(obj)
        self.assertIn("BaseModel.{}".format(obj.id), models.storage.all())

    def test_new_obj_none(self):
        """Test whether creating new object with None raises an AttributeError"""
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_new_obj_more_args(self):
        """Should raise a TypeError when additional arguments are provided"""
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), arg)

    def test_all_returns_dict(self):
        """Check whether the all method returns a dict"""
        self.assertEqual(dict, type(models.storage.all()))

    def test_save_reload(self):
        """Testing whether files are being saved"""
        obj_1 = BaseModel()
        obj_2 = BaseModel()
        models.storage.new(obj_1)
        models.storage.new(obj_2)
        models.storage.save()

        """Reloading"""
        new_instance = FileStorage()
        new_instance.reload()

        """Test if the new instances match the originals"""
        self.assertTrue(new_instance.all().get("BaseModel.{}".format(obj_1.id)) is not None)
        self.assertTrue(new_instance.all().get("BaseModel.{}".format(obj_2.id)) is not None)

    def test_save_to_file(self):
        """Checking if file saving is successful"""
        obj = BaseModel()
        models.storage.new(obj)
        models.storage.save()
        self.assertTrue(os.path.exists(models.storage._FileStorage__file_path))

    def test_reload_empty_file(self):
        """Reloading an empty file should raise a TypeError"""
        with self.assertRaises(TypeError):
            models.storage()
            models.storage.reload()


class TestInstantiation(unittest.TestCase):
    """Testing the instantiation of file_storage"""

    def test_with_no_args(self):
        """Testing with no arguments"""
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_with_args(self):
        """Creating whether when an instance is created with
            args raises a TypeError"""
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_if_its_instance(self):
        """if storage variable is an instance of the FileStorage class"""
        self.assertEqual(type(models.storage), FileStorage)


if __name__ == "__main__":
    unittest.main()
