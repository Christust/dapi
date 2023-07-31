from django.urls import path
from rest_framework.routers import DefaultRouter
from apps.branches import views

router = DefaultRouter()

router.register(r"", views.BranchesViewSet)

urlpatterns = [] + router.urls
