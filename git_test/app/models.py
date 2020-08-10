from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name
    