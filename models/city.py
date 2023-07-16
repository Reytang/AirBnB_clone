#!/usr/bin/python3
"""
Module for the City class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Inherits from the BaseModel
    Public class attributes:
        state_id: (str) will be State.id
        name:     (str)
    """
    state_id = ""
    name = ""
