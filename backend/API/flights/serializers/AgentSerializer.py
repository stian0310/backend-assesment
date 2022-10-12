from rest_framework import serializers

from API.flights.models import Agent


class AgentSerializer(serializers.ModelSerializer):

  class Meta:
    model = Agent
    fields = [
        'name',
        'rating'
    ]
