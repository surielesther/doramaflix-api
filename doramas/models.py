from django.db import models

class AgeRatingOptions(models.TextChoices):
    MORNING = "Matutino"
    AFTERNOON = "Vespertino"
    NIGHT = "Noturno"
    DEFAULT = "Não informado"

class GenreOptions(models.TextChoices):
    MORNING = "Matutino"
    AFTERNOON = "Vespertino"
    NIGHT = "Noturno"
    DEFAULT = "Não informado"


class Dorama(models.Model):

    name = models.CharField(max_length=40, unique=True)
    cast = models.CharField(max_length=200)
    synopsis = models.CharField(max_length=500)
    genre = models.CharField(
        max_length=50,
        choices=GenreOptions.choices,
        default=GenreOptions.DEFAULT,
        null=True,
    )
    release_year = models.IntegerField()
    age_rating = models.CharField(
        max_length=50,
        choices=AgeRatingOptions.choices,
        default=AgeRatingOptions.DEFAULT,
        null=True,
    )
    stars = models.IntegerField()

    REQUIRED_FIELDS = ['name', 'cast', 'synopsis', 'genre', 'release_year', 'age_rating', 'stars']

