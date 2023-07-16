#!/usr/bin/python3
"""
Module for the Review class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Inherits from BaseModel
    Public class attributes:
        user_id:             (str) will be User.id
        place_id:            (str) will be Place.id
        text:                (str)
    """
    user_id = ""
    place_id = ""
    text = ""

