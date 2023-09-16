from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255, default="", blank=True)
    author = models.CharField(max_length=255, default="", blank=True)
    date_added = models.DateField(auto_now_add=True)
    progress = models.CharField(max_length=255, default="", blank=True)
    amount = models.IntegerField(default="", blank=True)
    description = models.TextField(default="", blank=True)
