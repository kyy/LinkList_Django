from datetime import datetime
from django.db import models

class URL_list(models.Model):
    name = models.CharField(max_length=100)
    URL_long = models.TextField()
    URL_short = models.URLField(max_length=255)
    data = models.DateTimeField(default=datetime.now())

