from django.db import models
import datetime
from django.contrib.auth.models import User,auth

# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length = 100)
    priority = models.IntegerField()
    date = models.DateField(default = datetime.date.today)
    time = models.TimeField(auto_now_add = True)
    complete = models.BooleanField(default = False);
    owner = models.ForeignKey(User,on_delete = models.CASCADE)