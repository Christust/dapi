from django.urls import path
from rest_framework.routers import DefaultRouter
from apps.maintenance import views

router = DefaultRouter()

router.register(r"types", views.MaintenanceTypeViewSet)

urlpatterns = [] + router.urls
