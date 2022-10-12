from django.db import models

from API.flights.models import Agent, Leg


class Itinerary(models.Model):

    title = models.CharField(max_length=10, unique=True)
    legs = models.ManyToManyField(Leg)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "itineraries"
