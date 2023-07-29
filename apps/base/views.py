from rest_framework import viewsets, permissions
from django.shortcuts import get_object_or_404


class HasGroupPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        action = view.action
        permission_types = view.permission_types
        user_type = request.user.user_type
        required_user_types = permission_types.get(action)
        if user_type == "superadmin":
            return True
        elif "all" in required_user_types:
            return True
        elif required_user_types == None:
            return False
        else:
            return user_type in required_user_types


class BaseViewSet(viewsets.GenericViewSet):
    model = None
    serializer_class = None
    queryset = None
    permission_classes = [HasGroupPermission]
    permission_types = {}

    def get_object(self, pk):
        return get_object_or_404(self.queryset, pk=pk)
