import pyperclip
import string
import random

class User:
    """
    It will create the user class that generates instances of the user
    """
user_list = []

def __init__ (self, username, password):
    """
    It will create the method that defines properties of the user
    """
    self.username = username
    self.password = password

def save_user(self):
    """
    It will create the method that saves a new usert into the users list
    """
    User.user_list.append(self)

@classmethod
def display_user(cls):
    return cls.user_list

def delete_user(self):
    """
    It will create the method that deletes a user from the list, deletes saved account
    """
    User.user_list.remove(self)

class Credentials():
    """
    It will create the credentials class to create a new object of the credentials
    """
credentials_list = []
@classmethod
def verify_user(cls, username, password):
    """
    It will create a method to verify if the user is in the user list
    """
    a_user = ""
    for user in User.user_list:
        if(user.username == username and user.password == password):
            a_user == user.username
    return a_user

def __init__(self, account, userName, password):
    """
    It will create a method that defines user credentials to be stored
    """
    self.account = account
    self.userName = userName
    self.password = password

def save_details(self):
    """
    It will create a method that stores a new credential to the credential list
    """
    Credentials.credential_list.append(self)

def delete_credentials(self):
    """
    It will create a method that deletes credential from the credential list
    """
    Credentials.credential_list.remove(self)

@classmethod
def find_credentials(cls, account):
    """
    It will create a method that takes in a account_name and returns a credential that matches that account_name.
    """