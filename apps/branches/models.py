from django.db import models
from apps.base.models import Base
from apps.users.models import User


# Create your models here.
class Location(Base):
    name = models.CharField("Name", max_length=30, null=False, blank=False)

    def natural_key(self):
        return self.name

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Location"
        verbose_name_plural = "Locations"


class Branch(Base):
    name = models.CharField("Name", max_length=30, null=False, blank=False)
    location = models.ForeignKey(
        Location, on_delete=models.CASCADE, null=False, blank=False
    )
    users = models.ManyToManyField(User)

    def natural_key(self):
        return self.name

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Branch"
        verbose_name_plural = "Branches"


class Area(Base):
    name = models.CharField("Name", max_length=30, null=False, blank=False)
    branch = models.ForeignKey(
        Branch, on_delete=models.CASCADE, null=False, blank=False
    )

    def natural_key(self):
        return self.name

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Area"
        verbose_name_plural = "Areas"


class Subarea(Base):
    name = models.CharField("Name", max_length=30, null=False, blank=False)
    area = models.ForeignKey(Area, on_delete=models.CASCADE, null=False, blank=False)

    def natural_key(self):
        return self.name

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Subarea"
        verbose_name_plural = "Subareas"
