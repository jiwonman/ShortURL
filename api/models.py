from django.db import models
from django.utils.text import slugify
from sqids import sqids

# Create your models here.

class ShortURL(models.Model):
    key = models.CharField(max_length=10, primary_key=True, db_column='key')
    url = models.URLField()
    exp = models.DateTimeField(null=True)