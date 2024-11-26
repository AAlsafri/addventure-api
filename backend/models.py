from django.db import models
from django.contrib.auth.models import User

class Destination(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    continent = models.CharField(max_length=100)
    is_liked = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="destinations")


    def __str__(self):
        return self.name