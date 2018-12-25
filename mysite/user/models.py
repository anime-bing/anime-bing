from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profilepic = models.ImageField(upload_to='profile_pic',null=True,blank=True,default='default_profile_pic.jpg')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self,**kwargs):
        super().save()

        img = Image.open(self.profilepic.path)
        if img.height > 300 or img.width > 300:
            output = (300,300)
            img.thumbnail(output)
            img.save(self.profilepic.path)
