from django.db import models

# Create your models here.

class Voter(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    dob = models.DateField()
    nin = models.CharField(max_length=11)
    phone_no = models.CharField(max_length=15)
    vote = models.CharField(max_length=3)
    date_registered = models.DateTimeField(auto_now=True)

