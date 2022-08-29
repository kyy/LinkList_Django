from django.contrib.auth.models import User
from django.db import models
import datetime

class URL_list(models.Model):
    name = models.CharField(max_length=100)
    URL_long = models.TextField()
    URL_short = models.URLField(max_length=255)
    data = models.DateTimeField(default=datetime.datetime.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=3)

