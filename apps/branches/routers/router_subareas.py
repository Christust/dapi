from django.urls import path
from rest_framework.routers import DefaultRouter
from apps.branches.views import SubareaViewSet

router_subareas = DefaultRouter()

router_subareas.register(r"", SubareaViewSet)

urlpatterns = router_subareas.urls
