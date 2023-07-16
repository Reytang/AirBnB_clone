#!/usr/bin/python3
from datetime import datetime
from uuid import uuid4
import models

"""
Module of the BaseModel
Parent of all the classes
"""


class BaseModel():
    """Base class for the Airbnb clone project
    Methods:
        __init__(self, *args, **kwargs)
        __str__(self)
        __save(self)
        __repr__(self)
        to_dict(self)
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the attributes: random uuid, dates created/updated
        """
        if kwargs:
            for keys, val in kwargs.items():
                if "created_at" == keys:
                    self.created_at = datetime.strptime(kwargs["created_at"],
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif "updated_at" == keys:
                    self.updated_at = datetime.strptime(kwargs["updated_at"],
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif "__class__" == keys:
                    pass
                else:
                    setattr(self, keys, val)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Return string of info about model
        """
        return ('[{}] ({}) {}'.
                format(self.__class__.__name__, self.id, self.__dict__))

    def __repr__(self):
        """
        returns string representation
        """
        return (self.__str__())

    def save(self):
        """
        Update instance with updated time & save to serialized file
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Return dic with string formats of times; add class info to dic
        """
        dic1 = {}
        dic1["__class__"] = self.__class__.__name__
        for f, g in self.__dict__.items():
            if isinstance(g, (datetime, )):
                dic1[f] = g.isoformat()
            else:
                dic1[f] = g
        return dic1

