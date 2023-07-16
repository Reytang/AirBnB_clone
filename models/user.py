#!/usr/bin/python3
"""module class of the user class
"""

from models.base_model import BaseModel
import json


class User(BaseModel):
    """base model class
    Public class attributes:
        email:               (str)
        password:            (str)
        first_name:          (str)
        last_name:           (str)
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

