from rest_framework import viewsets

from .serializers import PlayerSerializer, TeamSerializer, CoachSerializer
from .models import Player, Team, Coach


class PlayerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows players to be viewed or edited.
    """
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class TeamViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows teams to be viewed or edited.
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class CoachViewSet(viewsets.ModelViewSet):
	"""
    API endpoint that allows teams to be viewed or edited.
    """
	queryset = Coach.objects.all()
	serializer_class = CoachSerializer
