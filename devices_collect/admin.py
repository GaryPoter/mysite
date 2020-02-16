from django.contrib import admin
from .models import Devices, Manufactory, CollectDevices, CollectType, AnalysisTask

# Register your models here.
admin.site.register(Devices)
admin.site.register(Manufactory)
admin.site.register(CollectType)
admin.site.register(CollectDevices)
admin.site.register(AnalysisTask)
