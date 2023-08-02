from django.urls import path
from rest_framework.routers import DefaultRouter
from apps.maintenance.views import MaintenanceTypeViewSet

router = DefaultRouter()

router.register(r"", MaintenanceTypeViewSet)

urlpatterns = router.urls
