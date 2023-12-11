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
from django.db.models import Q
from django.views.decorators.http import require_POST

import random

from . import models
# from . import serializers

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
    return redirect("index")


@csrf_exempt
@api_view(
    [
        "POST",
    ]
)
@permission_classes((AllowAny,))
def userRegister(request):
    email = request.data["email"]
    username = request.data["username"]
    password = request.data["password"]

    try:
        user = User.objects.create_user(
            email=email, username=username, password=password
        )

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
