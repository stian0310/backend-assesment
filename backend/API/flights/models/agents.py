from django.db import models


class Agent(models.Model):
    name = models.CharField(max_length=30, unique=True)
    rating = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} - Raiting {self.rating}'