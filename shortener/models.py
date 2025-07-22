from django.db import models
from .utils import generate_code

class ShortURL(models.Model):
    original_url = models.URLField()
    short_code = models.CharField(max_length=6, unique=True, default=generate_code)

    def __str__(self):
        return f"{self.short_code} -> {self.original_url}"