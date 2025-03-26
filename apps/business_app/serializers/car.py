from rest_framework import serializers

from apps.business_app.models.car import Car


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = (
            "id",
            "name",
            "model",
            "main_picture",
            "year",
            "seats",
            "mileage",
            "luggage",
            "air_conditioner",
            "extra_info",
            "enabled",
            "__str__",
        )
