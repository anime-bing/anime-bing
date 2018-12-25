from django.contrib.auth.models import User
from django.dispatch import reciever
from django.db.models.signals import post_save
from . models import Profile

@reciever(post_save,sender=User)
def create_profile(instance,created,**kwargs,sender):
    if created:
        Profile.Object.create(User=instance)

@reciever(post_save,sender=User)
def save_profile(instance,sender,**kwargs):
    instance.profile.save()
