from rest_framework import viewsets
from engagement.models import Club, Event
from engagement.serializers import ClubSerializer, EventSerializer


class ClubViewSet(viewsets.ModelViewSet):
    """
    retrieve:
    Return a single club.

    list:
    Return a list of clubs.
    """
    queryset = Club.objects.all()
    serializer_class = ClubSerializer
    http_method_names = ['get']


class EventViewSet(viewsets.ModelViewSet):
    """
    Return a list of events.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    http_method_names = ['get']
