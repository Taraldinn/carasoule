from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.

class Slider(models.Model):
    imagefield = CloudinaryField(folder="carousel/")
    Tittle = models.TextField()
    subtitle = models.TextField()
    button_url = models.URLField()


class Marketing(models.Model):
    imagefield = CloudinaryField(folder="carousel/")
    Tittle = models.TextField()
    subtitle = models.TextField()


class Feature(models.Model):
    imagefield = CloudinaryField(folder="carousel/")
    Tittle = models.TextField()
    subtitle = models.TextField()
