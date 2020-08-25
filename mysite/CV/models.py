from django.db import models

# Create your models here.

class Qualification(models.Model):
    text = models.TextField(default='')
