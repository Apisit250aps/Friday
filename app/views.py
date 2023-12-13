from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.

def pageLogin(request):
    
    return render(request, 'login.html')

@login_required
def pageIndex(request):
    
    return render(request, 'index.html')

@login_required
def pageGame(request, id):
    
    return render(request, 'game.html', {"id":id, "user":request.user.username})