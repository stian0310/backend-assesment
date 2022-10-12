from rest_framework import serializers

from API.flights.models import Itinerary
from API.flights.serializers import AgentSerializer

class ItinerarySerializerTwo(serializers.ModelSerializer):
  agent = AgentSerializer(read_only=True)

  class Meta:
    model = Itinerary
    fields = [
        'title',
        'agent',
        'price',
    ]