from django.urls import path
from rest_framework.routers import DefaultRouter
from apps.maintenance.views import MaintenanceReportViewSet

router = DefaultRouter()

router.register(r"", MaintenanceReportViewSet)

urlpatterns = router.urls
