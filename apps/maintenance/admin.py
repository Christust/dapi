from django.contrib import admin
from apps.maintenance.models import (
    MaintenanceType,
    MaintenanceRequest,
    MaintenanceReport,
)

# Register your models here.

admin.site.register(MaintenanceReport)
admin.site.register(MaintenanceRequest)
admin.site.register(MaintenanceType)
