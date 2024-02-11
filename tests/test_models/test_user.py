import unittest
import os
import models
from models.user import User
from models.base_model import BaseModel

class TestUser(unittest.TestCase):
    """
    Unittest for the instantiation of the User class
    """

    def test_attributes(self):
        """
        Check if the user attributes are empty strings
        """
        test_user = User()
        self.assertEqual(test_user.email, "")
        self.assertEqual(test_user.password, "")
        self.assertEqual(test_user.first_name, "")
        self.assertEqual(test_user.last_name, "")

    def setUp(self):
        """
        Create a temp file for saving
        """
        self.test_file = "test_file.json"
        models.storage.__file_path = self.test_file
        models.storage.save()

    def tearDown(self):
        """
        Remove the file after it's been tested
        """
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_if_parent_is_base_model(self):
        """
        Check if the User class successfully inherits from BaseModel
        """
        test_usr = User()
        self.assertTrue(issubclass(User, BaseModel))

    def test_implementation_of_attributes(self):
        """
        Check if the attributes have been implemented
        """
        test_user = User()
        test_user.email = "kingcornelius07@gmail.com"
        test_user.first_name = "Cornelius"
        test_user.last_name = "Ngure"
        test_user.password = "CorneliusNgure"

        user_string = str(test_user)

        self.assertIn("User", user_string)
        self.assertIn("kingcornelius07@gmail.com", user_string)
        self.assertIn("Cornelius", user_string)
        self.assertIn("Ngure", user_string)

    def test_user_to_dict(self):
        """
        Check if the attribute keys match the set value
        """
        test_user = User()
        test_user = User(email="kingcornelius07@gmail.com", password=
                "CorneliusNgure", first_name="Cornelius", last_name="Ngure")

        test_user.email = "kingcornelius07@gmail.com"
        test_user.first_name = "Cornelius"
        test_user.last_name = "Ngure"
        test_user.save()

        test_user_dict = test_user.to_dict()

        self.assertEqual(test_user_dict["email"], "kingcornelius07@gmail.com")
        self.assertEqual(test_user_dict["first_name"], "Cornelius")
        self.assertEqual(test_user_dict["last_name"], "Ngure")

    def test_creation_of_an_instance(self):
        """
        Test if attributes are accurately set
        """
        test_user = User(email="kingcornelius07@gmail.com", password=
                "CorneliusNgure", first_name="Cornelius", last_name="Ngure")

        self.assertEqual(test_user.email, "kingcornelius07@gmail.com")
        self.assertEqual(test_user.password, "CorneliusNgure")
        self.assertEqual(test_user.first_name, "Cornelius")
        self.assertEqual(test_user.last_name, "Ngure")

    def test_use_unique_id(self):
        """
        Check if the instances are generated using unique IDs
        """
        test_user_1 = User()
        test_user_2 = User()

        self.assertNotEqual(test_user_1.id, test_user_2.id)

if __name__ == "__main__":
    unittest.main()
