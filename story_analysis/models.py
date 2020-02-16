from django.db import models

# Create your models here.


class Story(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    workspace = models.ForeignKey('Workspace', on_delete=models.CASCADE, null=True)
    creator = models.ForeignKey('TestUser', on_delete=models.CASCADE, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    begin = models.DateTimeField()
    due = models.DateTimeField()
    size = models.IntegerField()
    priority = models.CharField(max_length=64)
    parent_id = models.CharField(max_length=64)
    type = models.CharField(max_length=64)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)
    iteration = models.ForeignKey('Iteration', on_delete=models.CASCADE, null=True)


class Workspace(models.Model):
    name = models.CharField(max_length=256)


class Category(models.Model):
    c_id = models.CharField(max_length=64)
    name = models.CharField(max_length=256)


class Iteration(models.Model):
    name = models.CharField(max_length=256)


class TestUser(models.Model):
    name = models.CharField(max_length=64)
    def __str__(self):
        return self.name