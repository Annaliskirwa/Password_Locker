#!/usr/bin/env python3.6
from passwordlock import User, Credentials

def create_new_user(username, password):
    """
    It will create a function that creates a new user with a username and password
    """
    new_user = User(username, password)
    return new_user

def save_user(user):
    """
    It will create a function that saves a new user
    """
    user.save_user()

def display_user():
    """
    It will create a function that displays an existing user
    """
    return User.display_user()

def login_user(username, password):
    """
    It will create a function that checks whether a user exist and then login the user in.
    """
    check_user = Credentials.verify_user(username, password)
    return check_user

def create_new_credential(account, userName, password):
    """
    It creates a function that creates new credentials for a given user account
    """
    new_credential = Credentials(account, userName, password)
    return new_credential

def save_credentials(credentials):
    """
    It creates a function that saves credentials to the credentials list
    """
    credentials.save_details()

def display_account_details():
    """
    It creates a function that returns all the saved credentials
    """
    return Credentials.display_credentials()

def delete_credential(credentials):
    """
    It creates a function that deletes credential from the credential list
    """
    credentials.delete_credentials()