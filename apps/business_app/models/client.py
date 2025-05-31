from django.db import models
from django.utils.translation import gettext_lazy as _


class Client(models.Model):
    first_name = models.CharField(verbose_name="Name", max_length=25)
    last_name = models.CharField(verbose_name="Name", max_length=100)
    email = models.EmailField(verbose_name="Email", unique=True)
    opinion = models.TextField(verbose_name=_("Opinion"))

    enabled = models.BooleanField(verbose_name=_("Enabled"), default=True)

    class Meta:
        verbose_name = _("Client")
        verbose_name_plural = _("Clients")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
