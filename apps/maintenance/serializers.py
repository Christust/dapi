from rest_framework import serializers
from apps.maintenance.models import MaintenanceType


class MaintenanceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceType
        exclude = ["is_active", "created_at", "modified_at", "deleted_at"]