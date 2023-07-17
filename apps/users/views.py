from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets, views
from rest_framework.decorators import action
from rest_framework_simplejwt.tokens import RefreshToken
from apps.users.serializers import (
    UserSerializer,
    UserOutSerializer,
    CustomTokenObtainPairSerializer,
    PasswordSerializer,
)
from apps.users.models import User
from rest_framework_simplejwt.views import TokenObtainPairView


class UserViewSet(viewsets.GenericViewSet):
    model = User
    serializer_class = UserSerializer
    out_serializer_class = UserOutSerializer
    queryset = serializer_class.Meta.model.objects.filter(is_active=True)

    def get_object(self, pk):
        return get_object_or_404(self.queryset, pk=pk)

    def list(self, request):
        users = self.queryset.all()
        users_out_serializer = self.out_serializer_class(users, many=True)
        return Response(data=users_out_serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        user_serializer = self.serializer_class(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            user_out_serializer = self.out_serializer_class(user_serializer.data)
            return Response(
                data=user_out_serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            data=user_serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE
        )

    def retrieve(self, request, pk):
        user = self.get_object(pk)
        user_out_serializer = self.out_serializer_class(user)
        return Response(data=user_out_serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk):
        user = self.get_object(pk)
        user_out_serializer = self.out_serializer_class(
            user, data=request.data, partial=True
        )
        if user_out_serializer.is_valid():
            user_out_serializer.save()
            return Response(
                data=user_out_serializer.data, status=status.HTTP_202_ACCEPTED
            )
        return Response(
            data=user_out_serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    @action(detail=True, methods=["post", "put"])
    def set_password(self, request, pk=None):
        user = self.get_object(pk)
        password_serializer = PasswordSerializer(data=request.data)
        if password_serializer.is_valid():
            user.set_password(password_serializer.validated_data["password"])
            user.save()
            return Response(
                data={"message": "Password updated"}, status=status.HTTP_200_OK
            )
        return Response(
            data=password_serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def destroy(self, request, pk):
        user = self.get_object(pk)
        user.is_active = False
        user.save()
        return Response(data={"message": "Deleted"}, status=status.HTTP_200_OK)


class Login(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        user = authenticate(username=username, password=password)
        if user and user.is_active:
            login_serializer = self.serializer_class(data=request.data)
            if login_serializer.is_valid():
                user_serializer = UserOutSerializer(user)
                return Response(
                    {
                        "token": login_serializer.validated_data.get("access"),
                        "refresh": login_serializer.validated_data.get("refresh"),
                        "user": user_serializer.data,
                    },
                    status.HTTP_200_OK,
                )
            return Response(
                {"error": "No existe el usuario"}, status=status.HTTP_400_BAD_REQUEST
            )
        return Response(
            {"error": "No existe el usuario"}, status=status.HTTP_400_BAD_REQUEST
        )


class Logout(views.APIView):
    serializer_class = None
    def post(self, request, *args, **kwargs):
        user = self.request.user
        if user:
            token = RefreshToken(request.data.get("refresh_token"))
            token.blacklist()
            return Response({"message": "Sesion cerrada"})
        return Response(
            {"error": "No existe el usuario"}, status=status.HTTP_400_BAD_REQUEST
        )
