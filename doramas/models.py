from django.db import models

class AgeRatingOptions(models.TextChoices):
    LIVRE = 'Livre'
    DEZ = '10'
    DOZE = '12'
    QUATORZE = '14'
    DEZESSEIS = '16'
    DEZOITO = '18'
    DEFAULT = 'Não informado'

class GenreOptions(models.TextChoices):
    MORNING = 'romance'
    AFTERNOON = 'escolar'
    NIGHT = 'comédia'
    POLICIAL = 'policial'
    MEDICINA = 'drama médico'
    FICÇAO = 'ficção científica'
    SUSPENSE = 'suspense'
    TERROR = 'terror'
    OUTRO = 'outro'
    DEFAULT = 'Não informado'


class Dorama(models.Model):

    name = models.CharField(max_length=40, unique=True)
    cast = models.CharField(max_length=200)
    synopsis = models.CharField(max_length=1500)
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
    trailer = models.URLField(max_length=300)
    poster = models.URLField(max_length=300)

    REQUIRED_FIELDS = ['name', 'cast', 'synopsis', 'genre', 'release_year', 'age_rating', 'stars', 'trailer', 'poster']

