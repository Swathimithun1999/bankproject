from django.db import models
class Branch(models.Model):
    name=models.CharField(max_length=250)
    password=models.IntegerField()
