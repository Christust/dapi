from rest_framework import serializers
from apps.maintenance import models


class MaintenanceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MaintenanceType
        exclude = ["is_active", "created_at", "modified_at", "deleted_at"]


class MaintenanceRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MaintenanceRequest
        exclude = ["is_active", "created_at", "modified_at", "deleted_at"]


class MaintenanceRequestOutSerializer(serializers.ModelSerializer):
    maintenance_type = serializers.StringRelatedField()
    user = serializers.StringRelatedField()
    branch = serializers.StringRelatedField()
    area = serializers.StringRelatedField()
    subarea = serializers.StringRelatedField()

    class Meta:
        model = models.MaintenanceRequest
        exclude = ["is_active", "created_at", "modified_at", "deleted_at"]


class MaintenanceReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MaintenanceReport
        exclude = ["is_active", "created_at", "modified_at", "deleted_at"]


class MaintenanceReportOutSerializer(serializers.ModelSerializer):
    maintenance_request = serializers.StringRelatedField()
    user = serializers.StringRelatedField()

    class Meta:
        model = models.MaintenanceReport
        exclude = ["is_active", "created_at", "modified_at", "deleted_at"]
