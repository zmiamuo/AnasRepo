

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import time

# Create your models here.
class website(models.Model) :
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    website_url=models.URLField(max_length=250,null=False)
    website_blocked=models.BooleanField(default=True)
    
    def __str__(self):
        return self.website_url


class DurationUsage(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    duration=models.IntegerField()
    usage=models.IntegerField()
    ip_address=models.CharField(max_length=255)
    def __str__(self):
        return str(self.duration)


class Availaible_ip(models.Model):
    Availaible_ip=models.CharField(max_length=255)

    def __str__(self):
        return self.Availaible_ip



class logs_generated(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    date=models.CharField(max_length=255)
    ip_address_src=models.CharField(max_length=50)
    ip_address_dst=models.CharField(max_length=50)

    action=models.CharField(max_length=255)


    
