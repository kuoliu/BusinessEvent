from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class User_More(models.Model):
    user = models.ForeignKey(User)
    description = models.TextField()
    pic = models.ImageField(upload_to="user_images", blank=True)

    def __unicode__(self):
        return self.text

class User_Random(models.Model):
    user = models.ForeignKey(User)
    random = models.CharField(max_length=256)
