from django.contrib import admin
from locking.admin import LockingAdminMixin

# Register your models here.

from .models import InsydoGuide


class MyInsydoGuideAdmin(LockingAdminMixin, admin.ModelAdmin):
    pass


admin.site.register(InsydoGuide, MyInsydoGuideAdmin)
