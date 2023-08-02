from rest_framework import serializers
from apps.branches.models import Branch, Area, Subarea
from apps.users.models import User


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        exclude = ["is_active", "created_at", "modified_at", "deleted_at"]


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        exclude = ["is_active", "created_at", "modified_at", "deleted_at"]


class AreaOutSerializer(serializers.ModelSerializer):
    branch = serializers.StringRelatedField()

    class Meta:
        model = Area
        exclude = ["is_active", "created_at", "modified_at", "deleted_at"]


class SubareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subarea
        exclude = ["is_active", "created_at", "modified_at", "deleted_at"]


class SubareaOutSerializer(serializers.ModelSerializer):
    area = serializers.StringRelatedField()

    class Meta:
        model = Subarea
        exclude = ["is_active", "created_at", "modified_at", "deleted_at"]
