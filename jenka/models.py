from __future__ import unicode_literals

from django.db import models

class Student(models.Model):
   name = models.CharField(max_length=30)
   standard = models.IntegerField()
