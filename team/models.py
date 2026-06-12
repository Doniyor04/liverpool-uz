from django.db import models


# Create your models here.
class Position(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=100, verbose_name="player name")
    position = models.ForeignKey(
        Position,
        on_delete=models.CASCADE,
        related_name="players",
        verbose_name="position",
    )
    about = models.TextField(verbose_name="about")
    year = models.PositiveIntegerField(verbose_name="player year")
    number = models.PositiveIntegerField(verbose_name="player number")
    country = models.CharField(max_length=100, verbose_name="player country")
    matches = models.PositiveIntegerField(verbose_name="matches")
    count = models.PositiveIntegerField(verbose_name="counts")
    image = models.ImageField(
        upload_to="media/", null=True, blank=True, verbose_name="Image"
    )

    def __str__(self):
        return self.name

    def get_stat_type(self):
        """Position turiga qarab statistika turini qaytaradi"""
        position_name = self.position.name.lower()
        stats = {
            "darvozabon": "qaytargan",
            "himoyachi": "to'sgan",
            "yarim himoyachi": "assist",
            "hujumchi": "gol",
        }
        return stats.get(position_name, "counts")

    @property
    def age(self):
        from datetime import date

        return date.today().year - self.year


class Staff(models.Model):
    name = models.CharField(max_length=100, verbose_name="name")
    about = models.TextField(verbose_name="about")
    position = models.CharField(max_length=100, verbose_name="position")
    image = models.ImageField(
        upload_to="media/", null=True, blank=True, verbose_name="Image"
    )
