#!/usr/bin/python3
<<<<<<< HEAD
"""Contains the Review model"""
=======
"""Defines the Review class."""
>>>>>>> 8862b7c1b5318466b0f24bee47e5dc68ccec074c
from models.base_model import BaseModel


class Review(BaseModel):
<<<<<<< HEAD
    """Implements the Review model"""
=======
    """Represent a review.

    Attributes:
        place_id (str): The Place id.
        user_id (str): The User id.
        text (str): The text of the review.
    """

>>>>>>> 8862b7c1b5318466b0f24bee47e5dc68ccec074c
    place_id = ""
    user_id = ""
    text = ""
