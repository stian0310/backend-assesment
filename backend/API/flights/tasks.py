import requests

from celery import shared_task

from API.flights.models import Agent, Airline, Airport, Leg, Itinerary


def send_request():
    url = 'https://raw.githubusercontent.com/Skyscanner/full-stack-recruitment-test/main/public/flights.json'
    response = requests.get(url=url)
    data = {}
    if response.status_code == 200:
        data = response.json()
    return data


@shared_task
def get_flights(*args, **kwargs):
    flights = send_request()
    for leg in flights['legs']:
        departure_airport, created_departure_airport = Airport.objects.get_or_create(
            title=leg['departure_airport'])
        arrival_airport, created_arrival_airport = Airport.objects.get_or_create(
            title=leg['arrival_airport'])
        airline, created_airline = Airline.objects.get_or_create(
            title=leg['airline_id'],
            defaults={'name': leg['airline_name']})
        Leg.objects.get_or_create(
            title=leg['id'],
            defaults={
                'departure_airport': departure_airport,
                'arrival_airport': arrival_airport,
                'airline': airline,
                'departure_time': leg['departure_time'],
                'arrival_time': leg['arrival_time'],
                'stops': leg['stops'],
                'duration_mins': leg['duration_mins']
            })
    for itinerary in flights['itineraries']:
        agent, created_agent = Agent.objects.get_or_create(
            name=itinerary['agent'],
            defaults={ 'rating': itinerary['agent_rating'] }
            )
        update_itinerary, created_itinerary = Itinerary.objects.get_or_create(
            title=itinerary['id'],
            defaults={
                'agent': agent,
                'price': itinerary['price'],
            })
        leg_1 = Leg.objects.get(title=itinerary['legs'][0])
        leg_2 = Leg.objects.get(title=itinerary['legs'][1])
        update_itinerary.legs.set([leg_1, leg_2])