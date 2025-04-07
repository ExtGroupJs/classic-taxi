from rest_framework import serializers

from apps.business_app.models.driver import Driver


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = (
            "id",
            "name",
            "car",
            "licence_year",            
            "main_picture",
            "enabled",
            "extra_info",
            "__str__",
        )
