#!/usr/bin/env python3.6
from passwordlock import User, Credentials

def create_new_user(username, password):
    """
    It will create a function that creates a new user with a username and password
    """
    new_user = User(username, password)
    return new_user