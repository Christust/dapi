from django.urls import path
from rest_framework.routers import DefaultRouter
from apps.branches.views import AreaViewSet

router_areas = DefaultRouter()

router_areas.register(r"", AreaViewSet)

urlpatterns = router_areas.urls
