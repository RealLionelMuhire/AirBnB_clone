#!/usr/bin/python3
<<<<<<< HEAD
"""Implements the user's model"""
=======
"""Defines the User class."""
>>>>>>> 8862b7c1b5318466b0f24bee47e5dc68ccec074c
from models.base_model import BaseModel


class User(BaseModel):
<<<<<<< HEAD
    """
    Inherits from the BaseModel class and add user's functionalities

    Args:
        email (str): the email of the user
        password (str): the password of the user
        first_name (str): the first name of the user
        last_name (str): the last name of the user
    """
=======
    """Represent a User.

    Attributes:
        email (str): The email of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """

>>>>>>> 8862b7c1b5318466b0f24bee47e5dc68ccec074c
    email = ""
    password = ""
    first_name = ""
    last_name = ""
