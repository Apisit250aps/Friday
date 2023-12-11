from django.shortcuts import render

# Create your views here.

def pageLogin(request):
    
    return render(request, 'login.html')

def pageIndex(request):
    
    return render(request, 'index.html')