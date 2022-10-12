from rest_framework import serializers

from API.flights.models import Itinerary
from API.flights.serializers import AgentSerializer, LegSerializer


class ItinerarySerializer(serializers.ModelSerializer):
  legs = LegSerializer(read_only=True, many=True)
  agent = AgentSerializer(read_only=True)

  class Meta:
    model = Itinerary
    fields = [
        'title',
        'legs',
        'agent',
        'price',
    ]
    