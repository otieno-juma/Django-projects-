from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import random

# Create your views here.
def home(request):
    return render(request,'home.html')

def passgen(request):
    cham = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        cham.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        cham.extend(list('!@#$%^&*()_+'))
    if request.GET.get('numbers'):
        cham.extend(list('0123456789')) 
    length = int(request.GET.get('length', 10))
    
    password = ''
    for x in range(length):
        password += random.choice(cham)
    
    return render(request, 'password.html', {'password': password})