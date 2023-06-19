from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import authenticate, login, logout


from rest_framework.decorators import api_view

# Create your views here.
def index(request):
    return HttpResponse(open('static/index.html'))