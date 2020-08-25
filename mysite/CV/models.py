from django.db import models

# Create your models here.

class Qualification(models.Model):
    text = models.TextField(default='')

class Experience(models.Model):
    text = models.TextField(default='')