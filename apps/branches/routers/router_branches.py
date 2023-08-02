from django.urls import path
from rest_framework.routers import DefaultRouter
from apps.branches.views import BranchViewSet

router_branches = DefaultRouter()

router_branches.register(r"", BranchViewSet)

urlpatterns = router_branches.urls
