#!/usr/bin/python3
from datetime import datetime
from uuid import uuid4
import models

"""
Module of the BaseModel
Parent of all the classes
"""


class BaseModel():
    """Base class for  the Airbnb clone assignment
    Methods:
        __init__(self, *args, **kwargs)
        __str__(self)
        __save(self)
        __repr__(self)
        to_dict(self)
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize attributes: random uuid(adress), dates created/updated
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
        Return the string of information about model
        """
        return ('[{}] ({}) {}'.
                format(self.__class__.__name__, self.id, self.__dict__))

    def __repr__(self):
        """
        returns the string of the representation
        """
        return (self.__str__())

    def save(self):
        """
        Update instance with updated time & save to the serialized file
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Return dic with string formats of times; add class info to dic
        """
        dic = {}
        dic["__class__"] = self.__class__.__name__
        for f, v in self.__dict__.items():
            if isinstance(v, (datetime, )):
                dic[f] = v.isoformat()
            else:
                dic[f] = v
        return dic

