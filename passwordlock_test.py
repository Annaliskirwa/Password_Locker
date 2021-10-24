import unittest
from passwordlock import User
from passwordlock import Credentials

class TestClass(unittest.TestCase):
    """
    It will create a  Test class that defines test cases for the User class.
    """
    def setUp(self):
        """
        It creates a method that runs before each individual test methods run.
        """
        self.new_user = User('Annalis', 'Ann000')

    def test_init(self):
        """
        It creates a test case to check if the object has been initialized correctly
        """
        self.assertEqual(self.new_user.username, 'Annalis')
        self.assertEqual(self.new_user.password, 'Ann000')

    def test_save_user(self):
        """
        It createss a test case to test if a new user instance has been saved into the User list
        """
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)