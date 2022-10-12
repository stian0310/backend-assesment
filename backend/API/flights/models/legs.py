from django.db import models

from API.flights.models import Airport, Airline


class Leg(models.Model):
    title = models.CharField(max_length=10, unique=True)
    departure_airport = models.ForeignKey(Airport, related_name='departure_airport', null=False, on_delete=models.CASCADE)
    arrival_airport = models.ForeignKey(Airport, related_name='arrival_airport', null=False, on_delete=models.CASCADE)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    stops = models.IntegerField()
    duration_mins = models.IntegerField()
    airline = models.ForeignKey(Airline, null=False, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.departure_airport} - {self.arrival_airport}'
