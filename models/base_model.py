#!/usr/bin/python3
"""
BaseModel - Module
BaseModel Parent class,
 """

import uuid
from datetime import datetime
import models


class BaseModel:
    """
    BaseModel class take care of the initialization,
    serialization and deserialization of instances
    """

    def __init__(self, *args, **kwargs):
        """Initialization of a BaseModel instance"""
        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for key, val in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    # Try parsing with microseconds, fallback to without microseconds
                    try:
                        setattr(self, key, datetime.strptime(val, "%Y-%m-%dT%H:%M:%S.%f"))
                    except ValueError:
                        setattr(self, key, datetime.strptime(val, "%Y-%m-%dT%H:%M:%S"))
                elif key != "__class__":
                    setattr(self, key, val)

    def __str__(self):
        """String representation of a BaseModel instance"""
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def __repr__(self):
        """
            Return string representation of BaseModel class
        """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """updates 'updated_at' instance with current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return dictionary representation of BaseModel class."""
        nw_dct = dict(self.__dict__)
        nw_dct['__class__'] = self.__class__.__name__
        nw_dct['created_at'] = self.created_at.isoformat(timespec='seconds')
        nw_dct['updated_at'] = self.updated_at.isoformat(timespec='seconds')

        return (nw_dct)
