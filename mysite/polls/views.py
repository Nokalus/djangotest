from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'home.html')

def second_page(request):
    return render(request, 'second_page.html')
