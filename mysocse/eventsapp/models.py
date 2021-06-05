from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class EventModel(models.Model):
    event_name = models.CharField(max_length = 128)
    organiser = models.ManyToManyField(User,related_name="organiser")
    description = models.TextField()
    participants = models.ManyToManyField(User,related_name="participants",blank=True,null=True)
    cover = models.ImageField(upload_to='images/')
