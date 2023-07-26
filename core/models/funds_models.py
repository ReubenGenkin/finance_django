from django.db import models


class Funds(models.Model):
    name = models.CharField(max_length=200)
