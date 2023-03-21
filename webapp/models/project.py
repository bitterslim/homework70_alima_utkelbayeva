from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Project(models.Model):
    title = models.CharField(verbose_name='Project Title',max_length=300, null=False,  blank=False)
    description = models.TextField(verbose_name='Description',max_length=1000,null=False,blank=False)
    start_date = models.DateField(verbose_name='Started at',null=False, blank=False)
    finish_date = models.DateField(verbose_name='Ended at',null=False,blank=True, default=None)
    user = models.ManyToManyField(User, related_name='projects', blank=True, verbose_name='User')
