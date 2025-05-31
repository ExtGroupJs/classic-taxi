from django.contrib import admin

from apps.business_app.models.brand import Brand
from apps.business_app.models.car import Car
from apps.business_app.models.driver import Driver
from apps.business_app.models.gallery_picture import GalleryPicture
from apps.business_app.models.global_site_data import GlobalSiteData
from apps.business_app.models.model import Model
from apps.business_app.models.client import Client
from solo.admin import SingletonModelAdmin


admin.site.register(GlobalSiteData, SingletonModelAdmin)


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
        "extra_info_es",
        "extra_info_en",
        "extra_info_fr",
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
        "extra_info_es",
        "extra_info_en",
        "extra_info_fr",
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
        "main_picture",
        "enabled",
        "extra_info_es",
        "extra_info_en",
        "extra_info_fr",
    ]
    fields = [
        "name",
        "car",
        "licence_year",
        "main_picture",
        "enabled",
        "extra_info_es",
        "extra_info_en",
        "extra_info_fr",
    ]


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    empty_value_display = "-empty-"
    list_display = [
        "id",
        "first_name",
        "last_name",
        "email",
        "opinion",
        "enabled",
    ]
    fields = [
        "first_name",
        "last_name",
        "email",
        "opinion",
        "enabled",
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
