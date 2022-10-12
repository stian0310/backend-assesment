from rest_framework import mixins, viewsets

from API.flights.models import Leg
from API.flights.serializers import LegSerializerTwo


class LegView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet):

    queryset = Leg.objects.all()
    serializer_class = LegSerializerTwo
    search_fields = ['airline__name',]
    filterset_fields = ['departure_airport__title', 'departure_airport', 'arrival_airport__title', 'arrival_airport']
