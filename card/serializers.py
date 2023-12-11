from rest_framework import serializers

from . import models


class RobinsonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Robinson
        fields = "__all__"


class DangerousSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Dangerous
        fields = "__all__"


class BossSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Boss
        fields = "__all__"


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Game
        fields = "__all__"


class deckRobinsonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.deckRobinson
        fields = "__all__"


class graveRobinsonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.graveRobinson
        fields = "__all__"


class deckBossSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.deckBoss
        fields = "__all__"
