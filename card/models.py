from django.db import models
from django.contrib.auth.models import User

# Create your models here.


ACTIVES = (
    # robinson
    (0, "none"),
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
    # ages
    (-1, "max = 0"),
    (-2, "health - 1"),
    (-3, "health - 2"),
    (-4, "stop"),
)

ACTIVES_BOSS = (
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
)

ABILITY_TYPE = ((1, "Normal"), (2, "Age"), (3, "Skill"))

LEVEL_CHOICES = (
    (1, "Easy"),
    (2, "Medium"),
    (3, "Hard"),
)


class Robinson(models.Model):
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
    life_point = models.IntegerField()
    active = models.IntegerField(choices=ACTIVES_BOSS)

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
    age = models.IntegerField(default=0)
    draw = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    start = models.DateTimeField(auto_now_add=True)
    end = models.DateTimeField(auto_now=True)
    score = models.IntegerField(default=0)
    round = models.IntegerField(default=0)
    


class deckRobinson(models.Model):
    card = models.ForeignKey(Robinson, on_delete=models.CASCADE)
    value = models.IntegerField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Deck"
        verbose_name_plural = "Decks"

    def __str__(self):
        return self.card

    def get_absolute_url(self):
        return reversed("Deck_detail", kwargs={"pk": self.pk})


class graveRobinson(models.Model):
    card = models.ForeignKey(Robinson, on_delete=models.CASCADE)
    value = models.IntegerField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "graveRobinson"
        verbose_name_plural = "graveRobinson"

    def __str__(self):
        return self.card

    def get_absolute_url(self):
        return reversed("graveRobinson_detail", kwargs={"pk": self.pk})

class deckBoss(models.Model):
    card = models.ForeignKey(Boss, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "deckBoss"
        verbose_name_plural = "deckBoss"

    def __str__(self):
        return self.card

    def get_absolute_url(self):
        return reversed("deckBoss_detail", kwargs={"pk": self.pk})
