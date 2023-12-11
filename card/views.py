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


# Customers


@csrf_exempt
@api_view(
    [
        "GET",
    ]
)
@permission_classes((AllowAny,))
def Test(request):
    return Response({"status": "หมา", "message": "หิว"})


# General API Shop
@csrf_exempt
@api_view(
    [
        "GET",
    ]
)
@permission_classes((AllowAny,))
def getRobinson(request):
    robinson_card = models.Robinson.objects.all()
    robinsonSerializer = serializers.RobinsonSerializer(robinson_card, many=True)
    data = robinsonSerializer.data

    return Response({"status": True, "data": data})


@csrf_exempt
@api_view(
    [
        "GET",
    ]
)
@permission_classes((AllowAny,))
def StartGame(request):
    user = User.objects.get(username=request.user.username)
    try:
        if models.Game.objects.filter(user=user, status=False):
            status = False
        else:
            game = models.Game.objects.create(user=user)
            card = models.Robinson.objects.filter(type=1)
            card_boss = models.Boss.objects.all()
            print(card)
            for i in range(18):
                card_ran = random.choice(card)
                if models.deckRobinson.objects.filter(game=game, card=card_ran):
                    models.deckRobinson.objects.filter(game=game, card=card_ran).update(
                        value=F("value") + 1
                    )

                else:
                    models.deckRobinson.objects.create(game=game, card=card_ran)

            for boss in random.choices(card_boss, k=2):
                models.deckBoss.objects.create(game=game, card=boss)

            status = True

    except Exception as e:
        print(e)
        status = "01"

    return Response({"status": status})


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
