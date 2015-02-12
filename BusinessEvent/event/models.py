from django.db import models

from django.contrib.auth.models import User

# role[1:star, 2:media, 3:enterprise, 4:event holder]
class User_More(models.Model):
    user = models.ForeignKey(User)
    description = models.TextField()
    pic = models.ImageField(upload_to="user_images", blank=True)
    role = models.IntegerField()
    classification = models.CharField(max_length=64)

    def __unicode__(self):
        return unicode(self.user)

class User_Random(models.Model):
    user = models.ForeignKey(User)
    random = models.CharField(max_length=256)

class Event(models.Model):
    name = models.TextField()
    tag = models.CharField(max_length=64)
    description = models.TextField()
    pic = models.ImageField(upload_to="event_images", blank=True)
    datetime = models.DateTimeField()
    place = models.CharField(max_length=64)

    def __unicode__(self):
        return self.name

class News(models.Model):
    event = models.ForeignKey(Event,null=True)
    media = models.ForeignKey(User)
    tag = models.CharField(max_length=32)
    title = models.CharField(max_length=64)
    abstract = models.CharField(max_length=128)
    content = models.TextField()
    pic = models.ImageField(upload_to="news_images", blank=True)
    check = models.BooleanField()
    datetime = models.DateTimeField()

    def __unicode(self):
        return self.abstract

class UserMore_Event(models.Model):
    user_more = models.ForeignKey(User_More)
    event = models.ForeignKey(Event)

class UserMore_News(models.Model):
    user_more = models.ForeignKey(User_More)
    news = models.ForeignKey(News)