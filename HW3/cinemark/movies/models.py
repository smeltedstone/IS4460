from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True)
    director = models.CharField(max_length=100, blank=True)
    release_year = models.CharField(max_length=50, blank=True)
    budget = models.CharField(max_length=50, blank=True)
    runtime = models.CharField(max_length=50, blank=True)
    rating = models.CharField(max_length=50, blank=True)
    genre = models.CharField(max_length=50, blank=True)
    image_url = models.URLField(max_length=300, blank=True)
    youtube_url = models.URLField(blank=True)

    def __str__(self):
        return self.title