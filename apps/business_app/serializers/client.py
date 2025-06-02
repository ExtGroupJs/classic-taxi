from rest_framework import serializers

from apps.business_app.models.client import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "opinion",
            "enabled",
            "__str__",
        )
