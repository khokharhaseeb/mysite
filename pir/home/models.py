from django.db import models
from django.utils import timezone


# Create your models here.
class contact_message(models.Model):
    Name = models.CharField(max_length=150)
    Email = models.CharField(max_length=150)
    Subject = models.CharField(max_length=150)
    Message = models.TextField(max_length=150)
    Date_submit = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.Subject
    
class medical_billing(models.Model):
    Name = models.CharField(max_length=150)
    Email = models.CharField(max_length=150)
    Subject = models.CharField(max_length=150)
    Message = models.TextField(max_length=150)
    Date_submit = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.Subject
    
class dental_billing(models.Model):
    Name = models.CharField(max_length=150)
    Email = models.CharField(max_length=150)
    Subject = models.CharField(max_length=150)
    Message = models.TextField(max_length=150)
    Date_submit = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.Subject

class credentialing(models.Model):
    Name = models.CharField(max_length=150)
    Email = models.CharField(max_length=150)
    Subject = models.CharField(max_length=150)
    Message = models.TextField(max_length=150)
    Date_submit = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.Subject



