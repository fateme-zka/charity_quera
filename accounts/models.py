from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    address = models.TextField(blank=True, null=True)
    age = models.PositiveSmallIntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    GENDER_CHOICES = (
        ('F', 'Female'),
        ('M', 'Male'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)

    def get_full_name(self):
        return "{} {}".format(self.first_name, self.last_name)
