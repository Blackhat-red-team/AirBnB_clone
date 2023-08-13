#!/usr/bin/python3
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:

    def __init__(self, *args, **kwargs):

        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for k, v in kwargs.items():
                if k != "__class__":
                    if k == "updated_at":
                        self.updated_at = datetime.fromisoformat(v)
                    elif k == "created_at":
                        self.created_at = datetime.fromisoformat(v)
                    else:
                        setattr(self, k, v)

    def __str__(self):

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        vmdict1 = {}
        for key, value in self.__dict__.items():
            if key == 'created_at' or key == 'updated_at':
                value = value.isoformat()
            vmdict1[key] = value
        vmdict1['__class__'] = self.__class__.__name__

        return vmdict1
