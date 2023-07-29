from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.decorators import action
from apps.base.views import BaseViewSet
from apps.maintenance import serializers

# Create your views here.


class MaintenanceTypeViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.MaintenanceTypeSerializer
    queryset = serializer_class.Meta.model.objects.filter(is_active=True)
