from django.db import models


# Create your models here.


ACTIVES = (
    (1, "health + 1"),
    (2, "health + 2"),
    (3, "card + 1"),
    (4, "card + 2"),
    (5, "destroy"),
    (6, "double"),
    (7, "copy"),
    (8, "phase"),
    (9, "sort"),
    (10, "swap 1"),
    (11, "swaps 2"),
    (12, "under"),
)

ABILITY_TYPE = ((1, "Normal"), (2, "Age"), (3, "Skill"))

LEVEL_CHOICES = (
    (1, "Easy"),
    (2, "Medium"),
    (3, "Hard"),
)


class Abilities(models.Model):
    name = models.CharField(max_length=255)
    power = models.IntegerField()
    active = models.IntegerField(choices=ACTIVES)
    spend = models.IntegerField(choices=((1, "1"), (2, "2")))
    type = models.IntegerField(choices=ABILITY_TYPE)


class Dangerous(models.Model):
    name = models.CharField(max_length=255)
    pick = models.IntegerField()
    life_point = models.IntegerField(default=0)


class Boss(models.Model):
    name = models.CharField(max_length=255)
    pick = models.IntegerField()

    class Meta:
        verbose_name = "Boss"
        verbose_name_plural = "Boss"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reversed("Boss_detail", kwargs={"pk": self.pk})


class Game(models.Model):
    life_point = models.IntegerField(default=20)
    level = models.IntegerField(choices=LEVEL_CHOICES, default=1)

    class Meta:
        verbose_name = "game"
        verbose_name_plural = "games"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reversed("game_detail", kwargs={"pk": self.pk})
