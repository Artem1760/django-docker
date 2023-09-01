from django.db import models

class Product(models.Model):
    attachment = models.FileField()
