from django.db import models
from accounts.models import User, UserProfile
from django.db.models.signals import pre_save, post_save
# Create your models here.

class Lead(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    # the foreignkey is placed in the leads models
    # because every lead has its own agent and not the other way around
    agent = models.ForeignKey('Agent', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Agent(models.Model):
    user = models.OneToOneField(User, related_name="leads", on_delete=models.CASCADE)
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.user.email


def user_profile_create_signal(sender, instance, created, *args, **kwargs):
    print('Creating a user profile using the signals')
    if created:
        UserProfile.objects.create(user=instance)



post_save.connect(user_profile_create_signal, sender=User)