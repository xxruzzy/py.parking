from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255)
    phone = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=255)




