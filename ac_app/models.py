from django.db import models

# Create your models here.
class Access(models.Model):
    #access_no = models.CharField(max_length=200)
    access_no = models.PositiveIntegerField(blank=True, null=True)