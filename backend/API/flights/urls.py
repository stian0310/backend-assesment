from django.urls import path
from rest_framework.routers import DefaultRouter

from API.flights.views import ItineraryView, LegView

router = DefaultRouter()

router.register(r'itineraries', ItineraryView, basename='itinerary')
router.register(r'legs', LegView, basename='leg')

urlpatterns =  [
] + router.urls