from django.db import models

# Create your models here.

class Qualification(models.Model):
    text = models.TextField(default='')
    date = models.TextField(default='')

class Experience(models.Model):
    text = models.TextField(default='')

class Skill(models.Model):
    text = models.TextField(default='')
