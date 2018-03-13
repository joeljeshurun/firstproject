from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email_id = models.EmailField(max_length=80, unique=True)

    def __str__(self):
        return self.first_name

class details(models.Model):
    add = models.CharField(max_length=200)

    def __str__(self):
        return self.add