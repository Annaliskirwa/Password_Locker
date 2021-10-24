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