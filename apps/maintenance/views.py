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

    def list(self, request):
        offset = int(self.request.query_params.get("offset", 0))
        limit = int(self.request.query_params.get("limit", 10))

        searched_objects = self.queryset.all()[offset : offset + limit]
        serializer_class = (
            self.out_serializer_class(searched_objects, many=True)
            if self.out_serializer_class
            else self.serializer_class(searched_objects, many=True)
        )
        return Response(data=serializer_class.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk):
        searched_object = self.get_object(pk)
        serializer_class = (
            self.out_serializer_class(searched_object)
            if self.out_serializer_class
            else self.serializer_class(searched_object)
        )
        return Response(data=serializer_class.data, status=status.HTTP_200_OK)

    def update(self, request, pk):
        searched_object = self.get_object(pk)
        serializer_class = (
            self.out_serializer_class(searched_object, data=request.data, partial=True)
            if self.out_serializer_class
            else self.serializer_class(searched_object, data=request.data, partial=True)
        )
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(data=serializer_class.data, status=status.HTTP_202_ACCEPTED)
        return Response(
            data=serializer_class.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def destroy(self, request, pk):
        searched_object = self.get_object(pk)
        searched_object.is_active = False
        searched_object.save()
        return Response(data={"message": "Deleted"}, status=status.HTTP_200_OK)


class MaintenanceRequestViewSet(BaseModelViewSet):
    serializer_class = serializers.MaintenanceRequestSerializer
    out_serializer_class = serializers.MaintenanceRequestOutSerializer
    queryset = serializer_class.Meta.model.objects.filter(is_active=True)
    permission_types = {
        "list": ["all"],
        "create": ["all"],
        "update": ["all"],
        "retrieve": ["all"],
        "destroy": ["all"],
    }

    def list(self, request):
        offset = int(self.request.query_params.get("offset", 0))
        limit = int(self.request.query_params.get("limit", 10))

        searched_objects = self.queryset.all()[offset : offset + limit]
        serializer_class = (
            self.out_serializer_class(searched_objects, many=True)
            if self.out_serializer_class
            else self.serializer_class(searched_objects, many=True)
        )
        return Response(data=serializer_class.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk):
        searched_object = self.get_object(pk)
        serializer_class = (
            self.out_serializer_class(searched_object)
            if self.out_serializer_class
            else self.serializer_class(searched_object)
        )
        return Response(data=serializer_class.data, status=status.HTTP_200_OK)

    def update(self, request, pk):
        searched_object = self.get_object(pk)
        serializer_class = (
            self.out_serializer_class(searched_object, data=request.data, partial=True)
            if self.out_serializer_class
            else self.serializer_class(searched_object, data=request.data, partial=True)
        )
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(data=serializer_class.data, status=status.HTTP_202_ACCEPTED)
        return Response(
            data=serializer_class.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def destroy(self, request, pk):
        searched_object = self.get_object(pk)
        searched_object.is_active = False
        searched_object.save()
        return Response(data={"message": "Deleted"}, status=status.HTTP_200_OK)


class MaintenanceReportViewSet(BaseModelViewSet):
    serializer_class = serializers.MaintenanceTypeSerializer
    out_serializer_class = serializers.MaintenanceReportOutSerializer
    queryset = serializer_class.Meta.model.objects.filter(is_active=True)
    permission_types = {
        "list": ["all"],
        "create": ["all"],
        "update": ["all"],
        "retrieve": ["all"],
        "destroy": ["all"],
    }

    def list(self, request):
        offset = int(self.request.query_params.get("offset", 0))
        limit = int(self.request.query_params.get("limit", 10))

        searched_objects = self.queryset.all()[offset : offset + limit]
        serializer_class = (
            self.out_serializer_class(searched_objects, many=True)
            if self.out_serializer_class
            else self.serializer_class(searched_objects, many=True)
        )
        return Response(data=serializer_class.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk):
        searched_object = self.get_object(pk)
        serializer_class = (
            self.out_serializer_class(searched_object)
            if self.out_serializer_class
            else self.serializer_class(searched_object)
        )
        return Response(data=serializer_class.data, status=status.HTTP_200_OK)

    def update(self, request, pk):
        searched_object = self.get_object(pk)
        serializer_class = (
            self.out_serializer_class(searched_object, data=request.data, partial=True)
            if self.out_serializer_class
            else self.serializer_class(searched_object, data=request.data, partial=True)
        )
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(data=serializer_class.data, status=status.HTTP_202_ACCEPTED)
        return Response(
            data=serializer_class.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def destroy(self, request, pk):
        searched_object = self.get_object(pk)
        searched_object.is_active = False
        searched_object.save()
        return Response(data={"message": "Deleted"}, status=status.HTTP_200_OK)
