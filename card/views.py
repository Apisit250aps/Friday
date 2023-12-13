from heapq import merge
from multiprocessing import Value
from pyexpat import model
from django.shortcuts import render

# Create your views here.


from django.shortcuts import render, redirect
import json
import pytz
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.staticfiles import finders
from django.db.models import Q, F
from django.views.decorators.http import require_POST

import random


from . import models

from . import serializers

# Create your views here.

# user


@csrf_exempt
@api_view(
    [
        "POST",
    ]
)
@permission_classes((AllowAny,))
def userLogin(request):
    username = request.data["username"]
    password = request.data["password"]

    user = authenticate(username=username, password=password)

    if user is not None:
        if user.is_active:
            status = True
            msg = "user is login"
            login(request, user)
        else:
            status = False
            msg = "Currently, This user is not active"
    else:
        status = False
        msg = "Error wrong username/password"

    return Response({"status": status, "message": msg})


@csrf_exempt
@api_view(
    [
        "GET",
    ]
)
@permission_classes((AllowAny, IsAuthenticated))
def userLogout(request):
    logout(request)
    return Response({"status": True})


@csrf_exempt
@api_view(
    [
        "POST",
    ]
)
@permission_classes((AllowAny,))
def userRegister(request):
    username = request.data["username"]
    password = request.data["password"]

    try:
        user = User.objects.create_user(username=username, password=password)

        if user:
            status = True
            message = "Register Successfully!"
        else:
            status = False
            message = "Register Fail!"

    except Exception as err:
        status = False
        message = "Something is error!"

        print(err)

    return Response({"status": status, "message": message})


@csrf_exempt
@api_view(
    [
        "GET",
    ]
)
@permission_classes((AllowAny,))
def getRobinson(request):
    robinson_card = models.Robinson.objects.all()
    robinsonSerializer = serializers.RobinsonSerializer(
        robinson_card, many=True)
    data = robinsonSerializer.data

    return Response({"status": True, "data": data})


# Start game
@csrf_exempt
@api_view(
    [
        "GET",
    ]
)
@permission_classes((AllowAny,))
def StartGame(request):
    user = User.objects.get(username=request.user.username)
    game_id = 0
    try:
        if models.Game.objects.filter(user=user, status=False):
            status = False
            game_id = models.Game.objects.filter(user=user, status=False)[0].id
        else:
            game = models.Game.objects.create(user=user)
            card = models.Robinson.objects.filter(type=1)
            card_boss = models.Boss.objects.all()
            print(card)
            for i in range(2):
                card_ran = random.choice(card)
                if models.deckRobinson.objects.filter(game=game, card=card_ran):
                    models.deckRobinson.objects.filter(game=game, card=card_ran).update(
                        value=F("value") + 1
                    )

                else:
                    models.deckRobinson.objects.create(
                        game=game, card=card_ran)

            for boss in random.choices(card_boss, k=2):
                models.deckBoss.objects.create(game=game, card=boss)

            game_id = game.id
            status = True

    except Exception as e:
        print(e)
        status = "01"

    return Response(
        {
            "status": status,
            "game_id": game_id,
        }
    )


@csrf_exempt
@api_view(
    [
        "GET",
    ]
)
@permission_classes((AllowAny,))
def DeleteGame(request):
    try:
        user = User.objects.get(username=request.user.username)
        models.Game.objects.filter(user=user, status=False).delete()
        status = True
    except:
        status = False

    return Response({"status": status})


# On game

@csrf_exempt
@api_view(
    [
        "POST",
    ]
)
@permission_classes((AllowAny,))
def GameData(request):
    game_id = models.Game.objects.filter(id=int(request.data["id"]))
    gameSerializer = serializers.GameSerializer(game_id, many=True)
    game_data = gameSerializer.data

    boss_id = models.deckBoss.objects.filter(
        game=models.Game.objects.get(id=int(request.data["id"]))
    )
    bossSerializer = serializers.deckBossSerializer(boss_id, many=True)
    boss_data = bossSerializer.data
    boss_list = []
    for boss in boss_data:
        boss = dict(boss)
        boss["card"] = serializers.BossSerializer(
            models.Boss.objects.get(id=int(boss["card"]))).data
        boss_list.append(boss)
    status = True

    return Response(
        {
            "status": status,
            "data": {
                "game": game_data[0],
                "boss": boss_list,
                "deck": sum([int(i.value) for i in models.deckRobinson.objects.filter(game=game_id[0].id)]),
            }
        }
    )


@csrf_exempt
@api_view(
    [
        "POST",
    ]
)
@permission_classes((AllowAny,))
def Draw(request):
    # user = User.objects.get(username=request.user.username)
    id = request.data["id"]
    game = models.Game.objects.get(id=id)

    if models.deckRobinson.objects.filter(game=game).count() > 0:

        card = pickCard(game)
        card_data = card
        sum_card = sum(
            [
                int(i.value)for i in models.deckRobinson.objects.filter(game=game)
            ]
        )

    else:
        models.Game.objects.filter(id=id).update(
            age=F("age") + 1
        )
        deck_grave = models.graveRobinson.objects.filter(game=game)
        for grave in deck_grave:
            card = models.Robinson.objects.get(id=int(grave.card.id))
            value = int(grave.value)
            models.deckRobinson.objects.create(
                game=game, card=card, value=value)
            models.graveRobinson.objects.filter(id=grave.id).delete()

        models.deckRobinson.objects.create(
            game=game,
            card=random.choice(
                models.Robinson.objects.filter(type=2)
            )
        )

        card = pickCard(game)
        sum_card = sum(
            [
                int(i.value)for i in models.deckRobinson.objects.filter(game=game)
            ]
        )
        card_data = card

    status = True

    models.Game.objects.get(id=id).update(
        life_point=F("life_point") - int(request.data("mode"))

    )

    if int(models.Game.objects.get(id=id).life_point) < 0:
        status = False

    return Response(
        {
            "card": card_data,
            "deck": sum_card,
            "status": status,
        }
    )


def pickCard(game):

    draw = random.choice(models.deckRobinson.objects.filter(game=game))
    card = models.Robinson.objects.get(id=int(draw.card.id))
    card_data = serializers.RobinsonSerializer(card).data

    if models.deckRobinson.objects.get(id=draw.id):
        models.deckRobinson.objects.filter(id=draw.id).update(
            value=F("value") - 1
        )

        card_ran = card

        if models.graveRobinson.objects.filter(game=game, card=card_ran):
            models.graveRobinson.objects.filter(game=game, card=card_ran).update(
                value=F("value") + 1
            )

        else:
            models.graveRobinson.objects.create(
                game=game, card=card_ran)

        if models.deckRobinson.objects.filter(id=draw.id, value=0):
            models.deckRobinson.objects.filter(
                id=draw.id, value=0).delete()

    return card_data


@csrf_exempt
@api_view(
    [
        "GET",
    ]
)
@permission_classes((AllowAny,))
def DangerousSkills(request):

    list_enemies = []
    ser_dan = serializers.DangerousSerializer(random.choices(
        models.Dangerous.objects.all(), k=3), many=True).data
    ser_skill = serializers.RobinsonSerializer(random.choices(
        models.Robinson.objects.filter(type=3), k=3), many=True).data

    for i in range(3):
        list_enemies.append(
            {
                "danger": ser_dan[i],
                "skill": ser_skill[i]
            }
        )

    return Response(
        {
            "data": list_enemies,
        }
    )


@csrf_exempt
@api_view(
    [
        "POST",
    ]
)
@permission_classes((AllowAny,))
def Fights(request):
    id = request.data["id"]
    game = models.Game.objects.get(id=id)

    # if int(request.data["status"]) == 1:
    #     models.graveRobinson.objects.create(
    #         game=game, card=models.Robinson.objects.filter(id=int(request.data["card_id"])))
    # else:
    #     fight_result = 0

    return Response(
        {
            "deck": sum([int(i.value) for i in models.deckRobinson.objects.filter(game=game)])
        }
    )
