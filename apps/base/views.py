from rest_framework import viewsets, permissions
from django.shortcuts import get_object_or_404


class HasGroupPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        permission_types = view.permission_types
        action = view.action
        required_user_types = permission_types.get(action)
        if "all" in required_user_types:
            return True
        else:
            user_type = request.user.user_type
            if user_type == "superadmin":
                return True
            elif required_user_types == None:
                return False
            else:
                return user_type in required_user_types


class BaseGenericViewSet(viewsets.GenericViewSet):
    model = None
    serializer_class = None
    queryset = None
    permission_classes = [HasGroupPermission]
    permission_types = {}
    searched_object = None

    def get_object(self, pk):
        return get_object_or_404(self.queryset, pk=pk)


class BaseModelViewSet(viewsets.ModelViewSet):
    model = None
    serializer_class = None
    queryset = None
    permission_classes = [HasGroupPermission]
    permission_types = {}
    searched_object = None

    def get_object(self, pk):
        return get_object_or_404(self.queryset, pk=pk)
