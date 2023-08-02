from django.urls import path
from rest_framework.routers import DefaultRouter
from apps.maintenance.views import MaintenanceRequestViewSet

router = DefaultRouter()

router.register(r"", MaintenanceRequestViewSet)

urlpatterns = router.urls
