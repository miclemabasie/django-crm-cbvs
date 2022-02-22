from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

# Create your models here.

class Lead(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    # the foreignkey is placed in the leads models
    # because every lead has its own agent and not the other way around
    agent = models.ForeignKey('Agent', on_delete=models.CASCADE)


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
