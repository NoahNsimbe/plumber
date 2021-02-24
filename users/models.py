from django.contrib.auth.models import User
from django.db import models


class Clients(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"

    def __str__(self):
        return str(self.user.get_full_name())


class Plumber(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    profile_picture = models.ImageField(blank=True, null=True)
    phone = models.CharField(max_length=13, blank=True, null=True)
    location = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Plumber"
        verbose_name_plural = "Plumbers"

    def __str__(self):
        return str(self.user.get_full_name())
