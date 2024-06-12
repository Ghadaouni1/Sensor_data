from django.db import models

class Patient(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=255)
    phone_number = models.CharField(max_length=20)
    age = models.IntegerField()
    height = models.DecimalField(max_digits=5, decimal_places=2)
    weight = models.DecimalField(max_digits=5, decimal_places=2)