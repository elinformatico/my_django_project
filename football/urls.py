from django.conf.urls import url, include

from rest_framework import routers

from .views import PlayerViewSet, TeamViewSet

router = routers.DefaultRouter()
router.register(r'players', PlayerViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'coachs', CoachViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]