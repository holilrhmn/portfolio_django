from django.db import models

#about me
from django import forms


class About(models.Model):
    objects = None
    short_description = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to="about")

    class Meta:
        verbose_name = "About Me"
        verbose_name_plural = "About Me"

    def __str__(self):
        return "About Me"

#service model
class Service(models.Model):
    objects = None
    name = models.CharField(max_length=100, verbose_name="Service Message")
    description = models.TextField(verbose_name="About Service")

    def __str__(self):
        return  self.name

class RecentWork(models.Model):
    objects = None
    title = models.CharField(max_length=100, verbose_name="Work Title")
    link = models.TextField(verbose_name="Link Project")
    image = models.ImageField(upload_to="works")

    def __str__(self):
        return self.title

#client model

class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name="Client Name")
    description = models.TextField(verbose_name="Client Say")
    image = models.ImageField(upload_to="clients", default="default.png")

    def __str__(self):
        return self.name