# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# Create your models here
class SubjectFaculty(models.Model):
    subject = models.CharField(max_length=50,unique=True)
    name = models.CharField(max_length=50)
    def n_subject(self):
        return self.all_subject.count()
    def __str__(self):
        return self.subject
class StudentMarks(models.Model):
    studentname = models.CharField(max_length=50)
    subject = models.ForeignKey(SubjectFaculty,related_name='all_subject',to_field = "subject",db_column ="subject",null=True,blank=True,on_delete=models.CASCADE)
    marks = models.IntegerField()

''' The above describe the fields of the SubjectFaculty table and StudentMarks table by using this and database.py we are Create a database in Mysql'''
