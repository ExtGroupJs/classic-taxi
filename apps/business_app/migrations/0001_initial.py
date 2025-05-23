# Generated by Django 5.1.6 on 2025-03-26 22:47

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Brand",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=25, unique=True, verbose_name="Name"),
                ),
                (
                    "logo",
                    models.ImageField(
                        blank=True, null=True, upload_to="", verbose_name="logo"
                    ),
                ),
            ],
            options={
                "verbose_name": "Brand",
                "verbose_name_plural": "Brands",
            },
        ),
        migrations.CreateModel(
            name="Car",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=25, unique=True, verbose_name="Name"),
                ),
                (
                    "main_picture",
                    models.ImageField(upload_to="", verbose_name="Main Picture"),
                ),
                (
                    "year",
                    models.PositiveSmallIntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(limit_value=1900)
                        ],
                        verbose_name="Year",
                    ),
                ),
                (
                    "seats",
                    models.PositiveSmallIntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(limit_value=2)
                        ],
                        verbose_name="Seats",
                    ),
                ),
                (
                    "mileage",
                    models.PositiveSmallIntegerField(
                        blank=True, null=True, verbose_name="Mileage"
                    ),
                ),
                (
                    "luggage",
                    models.PositiveSmallIntegerField(
                        blank=True, null=True, verbose_name="Luggage"
                    ),
                ),
                (
                    "air_conditioner",
                    models.BooleanField(default=True, verbose_name="Air conditioner"),
                ),
                ("enabled", models.BooleanField(default=True, verbose_name="Enabled")),
                (
                    "extra_info",
                    models.TextField(blank=True, null=True, verbose_name="Extra Info"),
                ),
            ],
            options={
                "verbose_name": "Car",
                "verbose_name_plural": "Cars",
            },
        ),
        migrations.CreateModel(
            name="Driver",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=25, unique=True, verbose_name="Name"),
                ),
                (
                    "main_picture",
                    models.ImageField(upload_to="", verbose_name="Main Picture"),
                ),
                (
                    "licence_year",
                    models.PositiveSmallIntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(limit_value=1900)
                        ],
                        verbose_name="Licence year",
                    ),
                ),
                ("enabled", models.BooleanField(default=True, verbose_name="Enabled")),
                (
                    "extra_info",
                    models.TextField(blank=True, null=True, verbose_name="Extra Info"),
                ),
                (
                    "car",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="car_drivers",
                        to="business_app.car",
                        verbose_name="car",
                    ),
                ),
            ],
            options={
                "verbose_name": "Driver",
                "verbose_name_plural": "Drivers",
            },
        ),
        migrations.CreateModel(
            name="GalleryPicture",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "picture",
                    models.ImageField(upload_to="", verbose_name="Main Picture"),
                ),
                (
                    "extra_info",
                    models.TextField(blank=True, null=True, verbose_name="Extra Info"),
                ),
                (
                    "car",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="car_gallery_pictures",
                        to="business_app.car",
                        verbose_name="car",
                    ),
                ),
            ],
            options={
                "verbose_name": "Gallery Picture",
                "verbose_name_plural": "Gallery Pictures",
            },
        ),
        migrations.CreateModel(
            name="Model",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=250, unique=True, verbose_name="Name"),
                ),
                (
                    "extra_info",
                    models.TextField(blank=True, null=True, verbose_name="Extra Info"),
                ),
                (
                    "brand",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="business_app.brand",
                        verbose_name="Brand",
                    ),
                ),
            ],
            options={
                "verbose_name": "Model",
                "verbose_name_plural": "Models",
            },
        ),
        migrations.AddField(
            model_name="car",
            name="model",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="business_app.model",
                verbose_name="Modelo",
            ),
        ),
    ]
