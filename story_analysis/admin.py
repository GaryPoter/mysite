from django.contrib import admin
from .models import TestUser, Category, Workspace, Iteration, Story

# Register your models here.
admin.site.register(TestUser)
admin.site.register(Category)
admin.site.register(Workspace)
admin.site.register(Iteration)
admin.site.register(Story)