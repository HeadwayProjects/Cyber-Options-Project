from django.db import models

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=50)
    course_price = models.IntegerField()
    course_description = models.TextField()
    category = models.CharField(max_length=150)