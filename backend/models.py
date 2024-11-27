from django.db import models
from django.contrib.auth.models import User

class Continent(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Destination(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    continent = models.ForeignKey(Continent, on_delete=models.SET_NULL, null=True, blank=True)
    is_liked = models.BooleanField(default=False)
    visited_date = models.DateField(null=True, blank=True)  # Added the visited_date field
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="destinations")

    def __str__(self):
        return self.name