from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from apps.base.views import BaseModelViewSet
from apps.maintenance import serializers

# Create your views here.


class MaintenanceTypeViewSet(BaseModelViewSet):
    serializer_class = serializers.MaintenanceTypeSerializer
    queryset = serializer_class.Meta.model.objects.filter(is_active=True)
    permission_types = {
        "list": ["all"],
        "create": ["all"],
        "update": ["all"],
        "retrieve": ["all"],
        "destroy": ["all"],
    }

    def retrieve(self, request, pk):
        maintenance_type = self.get_object(pk)
        maintenance_type_serializer = self.serializer_class(maintenance_type)
        return Response(
            data=maintenance_type_serializer.data, status=status.HTTP_200_OK
        )

    def update(self, request, pk):
        maintenance_type = self.get_object(pk)
        maintenance_type_serializer = self.serializer_class(
            maintenance_type, data=request.data, partial=True
        )
        if maintenance_type_serializer.is_valid():
            maintenance_type_serializer.save()
            return Response(
                data=maintenance_type_serializer.data, status=status.HTTP_202_ACCEPTED
            )
        return Response(
            data=maintenance_type_serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def destroy(self, request, pk):
        maintenance_type = self.get_object(pk)
        maintenance_type.is_active = False
        maintenance_type.save()
        return Response(data={"message": "Deleted"}, status=status.HTTP_200_OK)
