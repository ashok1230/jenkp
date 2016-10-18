from __future__ import unicode_literals

from django.db import models

class Student(models.Model):
   name = models.CharField(max_length=30)
   standard = models.IntegerField()
   marks = models.IntegerField(null=True, blank=True)
   def __unicode__(self):
	return self.name

class Teacher(models.Model):
   name = models.CharField(max_length=30)
   subject = models.CharField(max_length=20)

class Subject(models.Model):
    name = models.CharField(max_length=20)
    stan = models.CharField(max_length=30, null=True, blank=True)
    
