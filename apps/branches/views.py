from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from apps.base.views import BaseModelViewSet
from apps.branches import serializers

# Create your views here.


class BranchesViewSet(BaseModelViewSet):
    serializer_class = serializers.BranchSerializer
    queryset = serializer_class.Meta.model.objects.filter(is_active=True)
    permission_types = {
        "list": ["all"],
        "create": ["all"],
        "update": ["all"],
        "retrieve": ["all"],
        "destroy": ["all"],
    }

    def retrieve(self, request, pk):
        branch = self.get_object(pk)
        branch_serializer = self.serializer_class(branch)
        return Response(data=branch_serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk):
        branch = self.get_object(pk)
        branch_serializer = self.serializer_class(
            branch, data=request.data, partial=True
        )
        if branch_serializer.is_valid():
            branch_serializer.save()
            return Response(
                data=branch_serializer.data, status=status.HTTP_202_ACCEPTED
            )
        return Response(
            data=branch_serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def destroy(self, request, pk):
        branch = self.get_object(pk)
        branch.is_active = False
        branch.save()
        return Response(data={"message": "Deleted"}, status=status.HTTP_200_OK)
