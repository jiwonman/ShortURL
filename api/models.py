from django.db import models
from .utils import Base62
# Create your models here.

class ShortURL(models.Model):
    key = models.CharField(max_length=6, primary_key=True)
    url = models.URLField(unique=True)
    expired = models.DateTimeField(null=True)
    count = models.IntegerField(default=0)
    