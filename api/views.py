from rest_framework import viewsets, generics
from .models import Member, Team, Role, Update, Event
from .serializers import MemberSerializer, TeamSerializer, RoleSerializer, UpdateSerializer, EventSerializer
from knox.auth import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import list_route


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all().filter(alumnus=False)
    serializer_class = MemberSerializer
    http_method_names = ['get']

    @list_route()
    def single_member(self, request, name=None):
        print(name)
        serializer = self.get_serializer(Member.objects.all().filter(alumnus=False, user__name__iexact=name).first(), many=False)
        return Response(serializer.data)


class AlumniViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all().filter(alumnus=True)
    serializer_class = MemberSerializer
    http_method_names = ['get']


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    http_method_names = ['get']


class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    http_method_names = ['get']


class UpdateViewSet(viewsets.ModelViewSet):
    queryset = Update.objects.all()
    serializer_class = UpdateSerializer
    http_method_names = ['get']


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    http_method_names = ['get']


class ProtectedViewSet(generics.GenericAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        return Response({"secret_information": "this is a protected route"})
