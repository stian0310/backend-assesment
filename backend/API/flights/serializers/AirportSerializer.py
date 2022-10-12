from rest_framework import serializers

from API.flights.models import Airport


class AirportSerializer(serializers.ModelSerializer):

  class Meta:
    model = Airport
    fields = [
        'title',
    ]
