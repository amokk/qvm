from django.db import models

# Create your models here.

class VirtualMachine(models.Model):
    memory = models.PositiveSmallIntegerField()
    disk = models.PositiveSmallIntegerField()


