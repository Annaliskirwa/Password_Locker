import unittest
from passwordlock import User
from passwordlock import Credentials

class TestClass(unittest.TestCase):
    """
    It will create a  Test class that defines test cases for the User class.
    """
    def setUp(self):
        """
        It creates a method that runs before each individual user test methods run.
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

class TestCredentials(unittest.TestCase):
    """
    It creates a test class that defines test cases for credentials class
    """
    def setUp(self):
        """
        It creates a method that runs before each individual credential test methods run.
        """
        self.new_credential = Credentials('Email', 'Annalis', 'Ann000' )

    def test_init(self):
        """
        It will create a test case to check if a new Credentials instance has been initialized correctly
        """
        self.assertEqual(self.new_credential.account, 'Email')
        self.assertEqual(self.new_credential.userName, 'Annalis')
        self.assertEqual(self.new_credential.password,'Ann000')

    def save_credential_test(self):
        """
        It creates a test case to test if the crendential object is saved into the credentials list.
        """
        self.new_credential.save_details()
        self.assertEqual(len(Credentials.credentials_list),1)

    def tearDown(self):
        '''
        It creates a method that does clean up after each test case has run.
        '''
        Credentials.credentials_list = []

    def test_save_many_accounts(self):
        '''
        It creates a test to check if we can save multiple credentials objects to our credentials list
        '''
        self.new_credential.save_details()
        test_credential = Credentials("Twitter","Mickey","Mfh45hfk") 
        test_credential.save_details()
        self.assertEqual(len(Credentials.credentials_list),2)

    def test_delete_credential(self):
        """
        It creates a test method to test if we can remove an account credentials from our credentials_list
        """
        self.new_credential.save_details()
        test_credential = Credentials("Twitter","Mickey","Mfh45hfk")
        test_credential.save_details()

        self.new_credential.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_find_credentials(self):
        """
        test to check if we can find a credential entry by account name and display the details of the credential
        """
        self.new_credential.save_details()
        test_credential = Credentials("Twitter","Mickey","Mfh45hfk") 
        test_credential.save_details()

        the_credential = Credentials.find_credential("Twitter")

        self.assertEqual(the_credential.account,test_credential.account)

    def test_credential_exist(self):
        """
        test to check if we can return a true or false based on whether we find or can't find the credential.
        """
        self.new_credential.save_details()
        the_credential = Credentials("Twitter", "mikeycharles", "Mfh45hfk")  
        the_credential.save_details()
        credential_is_found = Credentials.if_credential_exist("Twitter")
        self.assertTrue(credential_is_found)

    def test_display_all_saved_credentials(self):
        '''
        It creates a method that displays all the credentials that has been saved by the user
        '''

        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)

if __name__ == "__main__":
    unittest.main()
