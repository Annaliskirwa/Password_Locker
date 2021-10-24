import random
import string
import pyperclip
class User:
    """
    It will create User class that generates new instances of a user.

    """
    user_list = []

    def __init__(self, username, password):
        """
        It creates a method that defines the properties of a user.
        """
        self.username = username
        self.password = password

    def save_user(self):
        """
        It creates a  method that saves a new user instace into the user list
        """
        User.user_list.append(self)
    

    @classmethod
    def display_user(cls):
        '''
        It creates a method that displays the users
        '''
        return cls.user_list

    def delete_user(self):
        '''
        It will create a delete_account method deletes a  saved account from the list
        '''
        User.user_list.remove(self)

class Credentials():
    """
    It creates a Create credentials class to help create new objects of credentials
    """
    credentials_list = []
    @classmethod
    def verify_user(cls,username, password):
        """
        It creates a method to verify whether the user is in our user_list
        """
        a_user = ""
        for user in User.user_list:
            if(user.username == username and user.password == password):
                    a_user == user.username
        return a_user

    def __init__(self,account,userName, password):
        """
       It creates a  method that defines user credentials to be stored
        """
        self.account = account
        self.userName = userName
        self.password = password
    
    def save_details(self):
        """
        It creates a method to store a new credential to the credentials list
        """
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        """
        It creates a delete_credentials method that deletes an account credentials from the credentials_list
        """
        Credentials.credentials_list.remove(self)
    
    @classmethod
    def find_credential(cls, account):
        """
        It creates a method that takes in a account_name and returns a credential that matches that account_name.

        """
        for credential in cls.credentials_list:
            if credential.account == account:
                return credential
    @classmethod
    def copy_password(cls,account):
        """
        It creates a method that allows one to copy their password using pyperclip
        """
        found_credentials = Credentials.find_credential(account)
        pyperclip.copy(found_credentials.password)

    @classmethod
    def if_credential_exist(cls, account):
        """
        It creates a method that checks if a credential exists from the credential list and returns true or false depending if the credential exists.
        """
        for credential in cls.credentials_list:
            if credential.account == account:
                return True
        return False
    @classmethod
    def display_credentials(cls):
        """
        It creates a method that returns all items in the credentials list

        """
        return cls.credentials_list

    def generatePassword(stringLength=8):
        """Generate a random password string of letters and digits and special characters"""
        password = string.ascii_uppercase + string.ascii_lowercase + string.digits + "~!@#$%^&*"
        return ''.join(random.choice(password) for i in range(stringLength))