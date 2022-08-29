from django.contrib.auth.models import User
from django.db import models
from datetime import datetime
import uuid


class URL_list(models.Model):
    name = models.CharField(max_length=100)
    URL_long = models.TextField()
    URL_short = models.URLField(default=uuid.uuid4, max_length=255)
    data = models.DateTimeField(default=datetime.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=3)


