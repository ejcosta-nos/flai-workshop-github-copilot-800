from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import Team, User, Activity, Leaderboard, Workout
from .serializers import (
    TeamSerializer, UserSerializer, ActivitySerializer,
    LeaderboardSerializer, WorkoutSerializer
)


@api_view(['GET'])
def api_root(request, format=None):
    """
    API root endpoint that provides links to all available endpoints
    """
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'teams': reverse('team-list', request=request, format=format),
        'activities': reverse('activity-list', request=request, format=format),
        'leaderboard': reverse('leaderboard-list', request=request, format=format),
        'workouts': reverse('workout-list', request=request, format=format),
    })


class TeamViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing Team instances
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing User instances
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ActivityViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing Activity instances
    """
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


class LeaderboardViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for viewing Leaderboard instances (read-only)
    """
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer


class WorkoutViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing Workout instances
    """
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
