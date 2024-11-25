from django.db import models

class Destination(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    continent = models.CharField(max_length=100)
    is_liked = models.BooleanField(default=False)

    def __str__(self):
        return self.name