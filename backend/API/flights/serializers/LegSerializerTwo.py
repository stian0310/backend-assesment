from rest_framework import serializers

from API.flights.models import Leg
from API.flights.serializers import AirportSerializer, AirlineSerializer, ItinerarySerializerTwo


class LegSerializerTwo(serializers.ModelSerializer):
  departure_airport = AirportSerializer(read_only=True)
  arrival_airport = AirportSerializer(read_only=True)
  airline = AirlineSerializer(read_only=True)
  itinerary_set = ItinerarySerializerTwo(read_only=True, many=True)

  class Meta:
    model = Leg
    fields = [
        'title',
        'departure_airport',
        'arrival_airport',
        'departure_time',
        'arrival_time',
        'stops',
        'duration_mins',
        'airline',
        'itinerary_set'
    ]
