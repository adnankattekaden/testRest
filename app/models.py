from django.db import models

# Create your models here.



class Hai(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)