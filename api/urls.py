from .views import MemberViewSet, AlumniViewSet, TeamViewSet, RoleViewSet, UpdateViewSet, EventViewSet, ProtectedViewSet
from django.urls import path

urlpatterns = [
    path("members/", MemberViewSet.as_view({'get': 'list'})),
    path("members/<slug:name>", MemberViewSet.as_view({'get': 'single_member'})),
    path("alumni/", AlumniViewSet.as_view({'get': 'list'})),
    path("teams/", TeamViewSet.as_view({'get': 'list'})),
    path("roles/", RoleViewSet.as_view({'get': 'list'})),
    path("updates/", UpdateViewSet.as_view({'get': 'list'})),
    path("events/", EventViewSet.as_view({'get': 'list'})),
    path("protected/", ProtectedViewSet.as_view())
]
