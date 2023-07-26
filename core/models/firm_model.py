from django.db import models

class FirmModel(models.Model):
    name = models.CharField(max_length=200)

