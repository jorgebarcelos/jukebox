from django.db import models


class Music(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    published_year = models.DateField()

    def __str__(self) -> str:
        return f'{self.title}:{self.artist}:{self.published_year}'
