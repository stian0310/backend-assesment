from rest_framework import serializers

from API.flights.models import Airline


class AirlineSerializer(serializers.ModelSerializer):

  class Meta:
    model = Airline
    fields = [
        'title',
        'name',
    ]
