from django.db import models

# Create your models here.


class UseLog(models.Model):
    test_user = models.ForeignKey('story_analysis.TestUser', on_delete=models.CASCADE, null=False)
    device = models.ForeignKey('IndoorDevices', on_delete=models.CASCADE, null=False)
    duration = models.FloatField()
    duration_req = models.FloatField


class IndoorDevices(models.Model):
    name = models.CharField(max_length=64)
    cpu_name = models.CharField(max_length=256)
    screen_size = models.CharField(max_length=64)
    system_os_v = models.CharField(max_length=64)
    manufactory = models.ForeignKey('devices_collect.Manufactory', on_delete=models.CASCADE, null=True)