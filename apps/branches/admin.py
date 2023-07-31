from django.contrib import admin
from apps.branches.models import Branch, Area, Subarea

# Register your models here.

admin.site.register(Branch)
admin.site.register(Area)
admin.site.register(Subarea)
