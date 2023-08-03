from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from apps.base.views import BaseModelViewSet
from apps.branches import serializers

# Create your views here.


class BranchViewSet(BaseModelViewSet):
    serializer_class = serializers.BranchSerializer
    queryset = serializer_class.Meta.model.objects.filter(is_active=True)
    permission_types = {
        "list": ["all"],
        "create": ["all"],
        "update": ["all"],
        "retrieve": ["all"],
        "destroy": ["all"],
    }

    def list(self, request):
        offset = int(self.request.query_params.get("offset", self.offset))
        limit = int(self.request.query_params.get("limit", self.limit))
        context = {"request": request}
        searched_objects = self.queryset.all()[offset : offset + limit]
        serializer_class = (
            self.out_serializer_class(searched_objects, many=True, context=context)
            if self.out_serializer_class
            else self.serializer_class(searched_objects, many=True, context=context)
        )
        return Response(data=serializer_class.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk):
        searched_object = self.get_object(pk)
        context = {"request": request}
        serializer_class = (
            self.out_serializer_class(searched_object, context=context)
            if self.out_serializer_class
            else self.serializer_class(searched_object, context=context)
        )
        return Response(data=serializer_class.data, status=status.HTTP_200_OK)

    def update(self, request, pk):
        searched_object = self.get_object(pk)
        context = {"request": request}
        serializer_class = self.serializer_class(
            searched_object, data=request.data, partial=True, context=context
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


class AreaViewSet(BaseModelViewSet):
    serializer_class = serializers.AreaSerializer
    out_serializer_class = serializers.AreaOutSerializer
    queryset = serializer_class.Meta.model.objects.filter(is_active=True)
    permission_types = {
        "list": ["all"],
        "create": ["all"],
        "update": ["all"],
        "retrieve": ["all"],
        "destroy": ["all"],
    }

    def list(self, request):
        offset = int(self.request.query_params.get("offset", self.offset))
        limit = int(self.request.query_params.get("limit", self.limit))
        context = {"request": request}
        searched_objects = self.queryset.all()[offset : offset + limit]
        serializer_class = (
            self.out_serializer_class(searched_objects, many=True, context=context)
            if self.out_serializer_class
            else self.serializer_class(searched_objects, many=True, context=context)
        )
        return Response(data=serializer_class.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk):
        searched_object = self.get_object(pk)
        context = {"request": request}
        serializer_class = (
            self.out_serializer_class(searched_object, context=context)
            if self.out_serializer_class
            else self.serializer_class(searched_object, context=context)
        )
        return Response(data=serializer_class.data, status=status.HTTP_200_OK)

    def update(self, request, pk):
        searched_object = self.get_object(pk)
        context = {"request": request}
        serializer_class = self.serializer_class(
            searched_object, data=request.data, partial=True, context=context
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


class SubareaViewSet(BaseModelViewSet):
    serializer_class = serializers.SubareaSerializer
    out_serializer_class = serializers.SubareaOutSerializer
    queryset = serializer_class.Meta.model.objects.filter(is_active=True)
    permission_types = {
        "list": ["all"],
        "create": ["all"],
        "update": ["all"],
        "retrieve": ["all"],
        "destroy": ["all"],
    }

    def list(self, request):
        offset = int(self.request.query_params.get("offset", self.offset))
        limit = int(self.request.query_params.get("limit", self.limit))
        context = {"request": request}
        searched_objects = self.queryset.all()[offset : offset + limit]
        serializer_class = (
            self.out_serializer_class(searched_objects, many=True, context=context)
            if self.out_serializer_class
            else self.serializer_class(searched_objects, many=True, context=context)
        )
        return Response(data=serializer_class.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk):
        searched_object = self.get_object(pk)
        context = {"request": request}
        serializer_class = (
            self.out_serializer_class(searched_object, context=context)
            if self.out_serializer_class
            else self.serializer_class(searched_object, context=context)
        )
        return Response(data=serializer_class.data, status=status.HTTP_200_OK)

    def update(self, request, pk):
        searched_object = self.get_object(pk)
        context = {"request": request}
        serializer_class = self.serializer_class(
            searched_object, data=request.data, partial=True, context=context
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
