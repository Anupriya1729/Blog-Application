
from django.db import models
from django.contrib.auth.models import User
from PIL import Image  
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self ,* args, **kwargs):  # overrides save method
        super(Profile, self).save(*args, **kwargs)
  # ,to run the super class save method

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
