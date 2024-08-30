from django.db import models

# Create your models here.
class Organization(models.Model):
    name = models.CharField(max_length=255)

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    role = models.CharField(max_length=255)
    organization = models.ForeignKey(Organization, blank=True, null=True, on_delete=models.SET_NULL)
    start_date = models.DateField()
    end_date = models.DateField()
    image = models.ImageField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    certificate = models.FileField(blank=True, null=True)

class Skill(models.Model):
    PROFICIENCY_LEVELS = (
        ('BEGINNER', 'Iniciante'),
        ('INTERMIDIATE', 'Intermediário'),
        ('ADVANCED', 'Avançado'),
    )
    
    name = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)
    proficiency = models.CharField(max_length=255, choices=PROFICIENCY_LEVELS)
    
class Honor(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    organization = models.ForeignKey(Organization, blank=True, null=True, on_delete=models.SET_NULL)
    certificate = models.FileField(blank=True, null=True)

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    institution = models.ForeignKey(Organization, blank=True, null=True, on_delete=models.SET_NULL)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now=True)
    certificate = models.FileField(blank=True, null=True)

