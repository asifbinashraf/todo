from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'user/index.html')
def login(request):
    return render(request, 'user/login.html')
def signup(request):
    return render(request, 'user/signup.html')
    
    