from django.contrib import admin

from API.flights.models import Airport, Airline, Leg, Agent, Itinerary

@admin.register(Airport)
class AirportAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title', )
    list_filter = ('updated_at', )

@admin.register(Airline)
class AirlineAdmin(admin.ModelAdmin):
    list_display = ('title', 'name', 'created_at', 'updated_at')
    search_fields = ('name', )
    list_filter = ('updated_at', )

@admin.register(Leg)
class LegAdmin(admin.ModelAdmin):
    list_display = ('departure_airport', 'arrival_airport', 'departure_time', 'arrival_time', 'stops', 'duration_mins', 'airline')
    search_fields = ('departure_airport', )
    list_filter = ('departure_airport', 'arrival_airport')

@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating', 'created_at', 'updated_at')
    search_fields = ('name', )
    list_filter = ('updated_at', )

@admin.register(Itinerary)
class ItineraryAdmin(admin.ModelAdmin):
    list_display = ('price', 'agent', 'get_legs')
    def get_legs(self,obj):
        return [leg for leg in obj.legs.all()]
    # search_fields = ('legs', )
    # list_filter = ('legs', )