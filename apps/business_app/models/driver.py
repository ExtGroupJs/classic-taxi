from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core import validators

from apps.business_app.models.car import Car


class Driver(models.Model):
    name = models.CharField(verbose_name="Name", unique=True, max_length=25)
    main_picture = models.ImageField(verbose_name=_("Main Picture"))

    licence_year = models.PositiveSmallIntegerField(
        verbose_name=_("Licence year"),
        validators=[validators.MinValueValidator(limit_value=1900)],
    )
    car = models.ForeignKey(
        to=Car,
        verbose_name="car",
        on_delete=models.CASCADE,
        related_name="car_drivers",
    )

    enabled = models.BooleanField(verbose_name=_("Enabled"), default=True)

    extra_info = models.TextField(verbose_name="Extra Info", null=True, blank=True)

    class Meta:
        verbose_name = _("Driver")
        verbose_name_plural = _("Drivers")

    def __str__(self):
        return f"{self.name}"
