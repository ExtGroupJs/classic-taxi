from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core import validators

from apps.business_app.models.model import Model


class Car(models.Model):
    name = models.CharField(verbose_name="Name", unique=True, max_length=25)

    model = models.ForeignKey(
        to=Model, verbose_name="Modelo", on_delete=models.CASCADE, null=True, blank=True
    )
    main_picture = models.ImageField(verbose_name=_("Main Picture"))

    year = models.PositiveSmallIntegerField(
        verbose_name=_("Year"),
        validators=[validators.MinValueValidator(limit_value=1900)],
    )
    seats = models.PositiveSmallIntegerField(
        verbose_name=_("Seats"),
        validators=[validators.MinValueValidator(limit_value=2)],
    )
    mileage = models.PositiveSmallIntegerField(
        verbose_name=_("Mileage"), null=True, blank=True
    )
    luggage = models.PositiveSmallIntegerField(
        verbose_name=_("Luggage"), null=True, blank=True
    )
    air_conditioner = models.BooleanField(
        verbose_name=_("Air conditioner"), default=True
    )
    enabled = models.BooleanField(verbose_name=_("Enabled"), default=True)

    extra_info = models.TextField(verbose_name="Extra Info", null=True, blank=True)

    class Meta:
        verbose_name = _("Car")
        verbose_name_plural = _("Cars")

    def __str__(self):
        return f"{self.name}"
