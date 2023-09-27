from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    #invisible data
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateField(auto_now_add=True)

    #visible data
    name = models.CharField(max_length=255, default="", blank=True)
    author = models.CharField(max_length=255, default="", blank=True)
    description = models.TextField(default="", blank=True)
    status = models.CharField( max_length=255, default="", blank=True)
    amount = models.IntegerField(default="", blank=True)
