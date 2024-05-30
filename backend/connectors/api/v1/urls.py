from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors135629ViewSet

router = DefaultRouter()
router.register(
    "testconnectors135629", Testconnectors135629ViewSet, basename="testconnectors135629"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]
