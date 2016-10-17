from __future__ import unicode_literals

from django.db import models

class Student(models.Model):
   name = models.CharField(max_length=30)
   standard = models.IntegerField()

class Teacher(models.Model):
   name = models.CharField(max_length=30)
   subject = models.CharField(max_length=20)

class Subject(models.Model):
    name = models.CharField(max_length=20)
    standard = models.CharField(max_length=20, null=True, blank=True)
