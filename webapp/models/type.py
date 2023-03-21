from django.db import models
from django.db.models import TextChoices


class TypeChoise(TextChoices):
    TASK = 'Task'
    BUG = 'Bag'
    ENHANCEMENT = 'Enhancement'
class Type(models.Model):
    type = models.CharField(max_length=100, choices=TypeChoise.choices, default=TypeChoise.TASK, null=False, blank=False, verbose_name='Type')

    def __str__(self) -> str:
        return self.type