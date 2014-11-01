from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class User_More(models.Model):
    user = models.ForeignKey(User)
    description = models.TextField()
    pic = models.ImageField(upload_to="user_images", blank=True)

    def __unicode__(self):
        return unicode(self.user)

class User_Random(models.Model):
    user = models.ForeignKey(User)
    random = models.CharField(max_length=256)

class Event(models.Model):
    name = models.TextField()
    description = models.TextField()
    pic = models.ImageField(upload_to="event_images", blank=True)

    def __unicode__(self):
        return self.name

class News(models.Model):
    event = models.ForeignKey(Event)
    media = models.ForeignKey(User)
    tag = models.CharField(max_length=32)
    title = models.CharField(max_length=64)
    abstract = models.CharField(max_length=128)
    content = models.TextField()
    pic = models.ImageField(upload_to="news_images", blank=True)
    check = models.BooleanField()

    def __unicode(self):
        return self.abstract