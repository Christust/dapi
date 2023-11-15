from django.contrib import admin
from django.urls import path, include

# Auth
from rest_framework_simplejwt.views import TokenRefreshView
from apps.users.views import Login, Logout


urlpatterns = [
    # Swagger
    path("", include("config.swagger_config")),
    # Auth
    path("login/", Login.as_view(), name="login"),
    path("logout/", Logout.as_view(), name="logout"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # Apps
    path("admin/", admin.site.urls),
    path("users/", include("apps.users.urls")),
    path("branches/", include("apps.branches.routers.router_branches")),
    path("areas/", include("apps.branches.routers.router_areas")),
    path("subareas/", include("apps.branches.routers.router_subareas")),
    path("maintenance_types/", include("apps.maintenance.routers.maintenance_types")),
    path(
        "maintenance_requests/",
        include("apps.maintenance.routers.maintenance_requests"),
    ),
    path(
        "maintenance_reports/", include("apps.maintenance.routers.maintenance_reports")
    ),
]
