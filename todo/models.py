import datetime

from django.utils import timezone
from django.db import models

# Create your models here.

class Person(models.Models):
  username = models.CharField(max_length=20)
  password = models.CharField(max_length=20)
  def __str__(self):
    return self.username

class Task(models.Models):
  person = models.ForeignKey(Person, on_delete=models.CASCADE)
  task_name = models.CharField(max_length=200)
  pub_date = models.datetime('date published')
  def __str__(self):
    return self.task_name

