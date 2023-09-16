from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255,default="no_name")
    author = models.CharField(max_length=255, default="no_author")
    date_added = models.DateField(auto_now_add=True)
    amount = models.IntegerField()
    description = models.TextField()
