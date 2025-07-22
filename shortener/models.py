from django.db import models

class ShortURL(models.Model):
    original_url = models.URLField()
    short_code = models.CharField(max_length=6, unique=True)

    def __str__(self):
        return f"{self.short_code} -> {self.original_url}"