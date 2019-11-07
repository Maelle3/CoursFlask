from app import  ma

from .models import Task


class TaskSchema(ma.ModelSchema):
    class Meta:
        model = Task
