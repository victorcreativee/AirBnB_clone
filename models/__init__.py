#!/usr/bin/python3
"""
__init__ for models directory
"""
from models.engine.file_storage import FileStorage
"""
Create the storage object
"""
storage = FileStorage()
"""
Import classes AFTER storage is defined to avoid circular imports
"""
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
"""
Define the classes dictionary
"""
classes = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review
}
"""
Call reload AFTER defining classes
"""
storage.reload()
