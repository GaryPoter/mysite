from django.db import models
from django.utils import timezone

# Create your models here.

'''
device_name varchar
rate float
cpu_name varchar
screen_size varchar
system_os_v varchar
manufactory int
'''

class Devices(models.Model):
    device_name = models.CharField(max_length=256)
    rate = models.FloatField()
    cpu_name = models.CharField(max_length=256)
    screen_size = models.CharField(max_length=64)
    system_os_v = models.CharField(max_length=64)
    manufactory = models.ForeignKey('Manufactory', on_delete=models.CASCADE, null=True)


'''
厂商
'''
class Manufactory(models.Model):
    manufactory_name = models.CharField(max_length=64)


'''
收集分析结果
collect_type: True:安卓;False: iOS
result: 生成列表，id,分割
generated_time: 生成的时间
'''
class CollectDevices(models.Model):
    collect_type = models.ForeignKey('CollectType', on_delete=models.CASCADE, null=False)
    result = models.CharField(max_length=256)
    generated_time = models.DateTimeField(default=timezone.now())


'''
分析类型
'''
class CollectType(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return '%s, %s' % (self.id, self.name)


'''
任务表
'''
class AnalysisTask(models.Model):
    name = models.CharField(max_length=256)
    created_time = models.DateTimeField(default=timezone.now())
    creator = models.ForeignKey('story_analysis.TestUser', on_delete=models.CASCADE, null=False)
    result = models.ForeignKey('CollectDevices', on_delete=models.CASCADE, null=False)