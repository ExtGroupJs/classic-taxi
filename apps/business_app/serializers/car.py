from rest_framework import serializers

from apps.business_app.models.car import Car


class CarSerializer(serializers.ModelSerializer):
    model_name = serializers.CharField(source="model.__str__")
    extra_info = serializers.CharField(read_only=True)

    class Meta:
        model = Car
        fields = (
            "id",
            "name",
            "model",
            "model_name",
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
