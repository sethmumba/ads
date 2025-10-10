from django.db import models

class Anime(models.Model):
    GENRES = [
        ('Action', 'Action'),
        ('Adventure', 'Adventure'),
        ('Comedy', 'Comedy'),
        ('Drama', 'Drama'),
        ('Fantasy', 'Fantasy'),
        ('Romance', 'Romance'),
        ('Sci-Fi', 'Sci-Fi'),
        ('Horror', 'Horror'),
        ('Slice of Life', 'Slice of Life'),
    ]

    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=50, choices=GENRES)
    rating = models.FloatField(default=0.0)
    synopsis = models.TextField()
    image = models.URLField(max_length=500, blank=True, null=True)
    release_year = models.IntegerField(default=2024)

    def __str__(self):
        return self.title
