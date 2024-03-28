from django.db import models

# Create your models here.
class TextQuery(models.Model):
    name = models.CharField(max_length = 32)