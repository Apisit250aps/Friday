"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from . import views

urlpatterns = [
    path("login", views.userLogin, name='login-api'),
    path("register", views.userRegister, name='register-api'),
    path("logout", views.userLogout, name='logout-api'),
    path("robinson", views.getRobinson),
    path("table", views.StartGame, name='newgame-api'),
    path("data", views.GameData, name="game-data-api"),
    path("draw", views.Draw),
    path("endgame", views.DeleteGame),
    path("danger", views.DangerousSkills, name="danger-api"),
    path("fight", views.Fights, name="fight-api"),
]
