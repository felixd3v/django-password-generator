from django.shortcuts import render
from django.http import HttpResponse

import random 

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')

def pw(request):
    
    letters = list('abcdefghijklmnopqrstuvxywz')
    
    if request.GET.get('uppercase'):
        letters.extend(list('ABCDEFGHIJKLMNOPQRSTUVXYWZ'))

    if request.GET.get('special_characters'):
        letters.extend(list('$%/()=!?><'))

    if request.GET.get('numbers'):
        letters.extend(list('0123456789'))   

    length = int(request.GET.get('length', 16))

    user_password = ''
    for item in range(length):
        user_password = user_password + random.choice(letters)
    return render(request, 'generator/pw.html', {'password':user_password})