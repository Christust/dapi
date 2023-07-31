from django.contrib import admin
from django.urls import path, include

# Auth
from rest_framework_simplejwt.views import TokenRefreshView
from apps.users.views import Login, Logout


urlpatterns = [
    # Swagger
    path("", include("dapi.swagger_config")),
    # Auth
    path("login/", Login.as_view(), name="login"),
    path("logout/", Logout.as_view(), name="logout"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # Apps
    path("admin/", admin.site.urls),
    path("users/", include("apps.users.urls")),
    path("maintenance/", include("apps.maintenance.urls")),
    path("branches/", include("apps.branches.urls")),
]
