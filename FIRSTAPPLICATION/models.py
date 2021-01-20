from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=15)
    eID = models.IntegerField(default=0)
    Address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Staff(models.Model):
    name = models.CharField(max_length=15)
    email = models.EmailField(max_length=20)
    eID = models.IntegerField()

    def __str__(self):
        return self.name

class Support(models.Model):
    fname = models.CharField(max_length=15)
    lname = models.CharField(max_length=15)
    eID = models.IntegerField()

    def __str__(self):
        return self.fname