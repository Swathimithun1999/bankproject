from django.db import models
class MoreDetail(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phoneNumber = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=100)
    district = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    account= models.CharField(max_length=50)
    material = models.CharField(max_length=50)
    class Meta:
        db_table = 'MoreDetail'

