from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import authenticate, login, logout
from .models import *


from rest_framework.decorators import api_view

# Create your views here.

def index(request):
    return HttpResponse(open('static/index.html'))

@api_view(["POST"])
def user_sign_up(request):
    email = request.data['email']
    password = request.data['password']
    handle = request.data['handle']
    super_user = False
    staff = False

    if 'super' in request.data:
        super_user = request.data['super']

    if 'staff' in request.data:
        staff = request.data['staff']

    if email == '' or password == '' or handle == '':
        return JsonResponse({"success": False, "reason": "empty field"})

    try:
        new_user = App_User.objects.create_user(
            username=handle, handle=handle, email=email, password=password)
        new_user.save()
        return JsonResponse({"success": True, "note": f"{handle} has been created"})
    except Exception as e:
        print(e)
        return JsonResponse({"success": False, "reason": "already signed up"})
    
@api_view(["POST"])
def user_sign_in(request):
    handle = request.data['handle']
    password = request.data['password']
    print(handle, password)
    print(request._request)
    user = authenticate(username=handle, password=password)
    print(user)
    if user is not None and user.is_active:
        try:
            login(request._request, user)
            print('logged in')
            return JsonResponse({"success": True, "note": f"{handle} has logged in"})
        except Exception as e:
            print(e)
            return JsonResponse({"success": False, "reason": e})
    print('other')
    return JsonResponse({"success": False, "reason": "user null/inactive error"})

@api_view(['POST'])
def user_sign_out(request):
    try:
        logout(request)
        return JsonResponse({"success": True, "note": "user has logged out"})
    except Exception as e:
        print(e)
        return JsonResponse({"success": False, "reason": e})