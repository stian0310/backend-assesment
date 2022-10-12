from rest_framework import mixins, viewsets

from API.flights.models import Itinerary
from API.flights.serializers import ItinerarySerializer


class ItineraryView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet):

    queryset = Itinerary.objects.all()
    serializer_class = ItinerarySerializer
    search_fields = ['legs__airline__name',]
    filterset_fields = ['legs__departure_airport__title', 'legs__departure_airport', 'legs__arrival_airport__title', 'legs__arrival_airport']
