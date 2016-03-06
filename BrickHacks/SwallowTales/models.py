from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    user = models.OneToOneField(User)
    def __str__(self):
        return "{0}".format(self.user.username)

class Story(models.Model):
    author = models.ForeignKey(User)
    name = models.CharField(max_length = 100)
    def __str__(self):
        return "{0}".format(self.name)

class StorySection(models.Model):
    previousSection = models.ForeignKey("self",null = True, blank=True, related_name="children")
    author = models.ForeignKey(User)
    story = models.ForeignKey(Story)
    secName = models.CharField(max_length = 100)
    text = models.TextField()

class Bookmark(models.Model):
    user = models.ForeignKey(User)
    section = models.ForeignKey(StorySection)