from django.db import models


class Customer(models.Model):
    username = models.EmailField(primary_key=True)
    password = models.CharField(max_length=32)


