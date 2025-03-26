from django.contrib import admin

from apps.business_app.models.brand import Brand
from apps.business_app.models.car import Car
from apps.business_app.models.driver import Driver
from apps.business_app.models.gallery_picture import GalleryPicture
from apps.business_app.models.model import Model


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    empty_value_display = "-empty-"
    list_display = [
        "id",
        "name",
        "logo",
    ]
    fields = [
        "name",
        "logo",
    ]


@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    empty_value_display = "-empty-"
    list_display = [
        "id",
        "name",
        "brand",
        "extra_info",
    ]
    fields = [
        "name",
        "brand",
        "extra_info",
    ]


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    empty_value_display = "-empty-"
    list_display = (
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
    )
    fields = [
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
    ]


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    empty_value_display = "-empty-"
    list_display = [
        "id",
        "name",
        "car",
        "licence_year",
        "enabled",
        "extra_info",
    ]
    fields = [
        "name",
        "car",
        "licence_year",
        "enabled",
        "extra_info",
    ]


@admin.register(GalleryPicture)
class GalleryPictureAdmin(admin.ModelAdmin):
    empty_value_display = "-empty-"
    list_display = [
        "id",
        "car",
        "picture",
        "extra_info",
    ]
    fields = [
        "car",
        "picture",
        "extra_info",
    ]
