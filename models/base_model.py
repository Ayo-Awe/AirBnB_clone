"""Base Model Module """
import uuid
from datetime import datetime


class BaseModel:
    """Base Model Class
        The base model class is the base for
        all other classes
    """

    def __init__(self):
        """Constructor for baseModel"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def __str__(self):
        """String representation of object instance"""
        return f"[{self.__class__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Save function
        Updates the update_at instance attribute
        """
        self.updated_at = datetime.today()

    def to_dict(self):
        """to_dict function
        Returns a dictionary containing all keys/values of
        __dict__ of the instance
        """
        new_dict = self.__dict__.copy()
        new_dict["updated_at"] = new_dict["updated_at"].isoformat()
        new_dict["created_at"] = new_dict["created_at"].isoformat()
        new_dict["__class__"] = self.__class__.__name__

        return new_dict
