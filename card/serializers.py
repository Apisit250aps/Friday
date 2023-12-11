from rest_framework import serializers

from . import models


class RobinsonSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Robinson
        fields = "__all__"