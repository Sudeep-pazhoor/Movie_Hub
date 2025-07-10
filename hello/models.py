from django.db import models
from django.utils import timezone

class Movie(models.Model):
    name = models.CharField(max_length=200)
    image_url = models.URLField("Image URL")
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    release_date = models.DateField()
    youtube_trailer = models.URLField("YouTube Trailer", blank=True)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} ({self.release_date})"
