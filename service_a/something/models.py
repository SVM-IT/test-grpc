from django.db import models


class Something(models.Model):
    title = models.CharField(max_length=255)
    something_from_another_service = models.CharField(max_length=255, null=True, blank=True)
