from django.db import models


class Assets(models.Model):
    name = models.CharField(max_length=200)
