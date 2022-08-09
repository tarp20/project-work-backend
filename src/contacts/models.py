from django.db import models
from django.db.models import Value
from django.db.models.functions import Substr, StrIndex


class Contact(models.Model):
    """ Stores sales Contact information """

    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=2155, blank=True, null=True)
    address = models.CharField(max_length=2155, blank=True, null=True)
    appearance = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return f'{self.name} {self.phone}'

    def get_appear(self, save=True):
        self.appearance += 1
        if save:
            self.save()

    def get_surname(self):
        return self.name.split()[1]
