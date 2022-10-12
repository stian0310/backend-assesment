from django.db import models


class Airline(models.Model):
    title = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
