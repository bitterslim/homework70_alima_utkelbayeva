from django.db import models
from django.db.models import TextChoices


class StatusChoise(TextChoices):
    IN_PROGRESS = 'In progress'
    NEW = 'New'
    DONE = 'Done'
class Status(models.Model):
    status = models.CharField(max_length=100, choices=StatusChoise.choices, default=StatusChoise.NEW, null=False, blank=False, verbose_name='Status')

    def __str__(self) -> str:
        return self.status