from rest_framework import serializers
from apps.branches.models import Branch


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        exclude = ["is_active", "created_at", "modified_at", "deleted_at"]
