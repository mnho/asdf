from django.db import models

# Create your models here.
class Record(models.Model):
  username =
    models.CharField(max_length=200)
  category =
    models.CharField(max_length=200)
