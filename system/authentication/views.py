
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from django.contrib.auth.models import User
from django.contrib import messages
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, logout, login


@api_view(['DELETE']) 
@renderer_classes([JSONRenderer]) 
def delete_user(request, user):
    u=User.objects.filter(username = user)
    u.delete()
    return Response("delete user " + user)


@api_view(['POST']) 
@renderer_classes([JSONRenderer]) 
def signup(request):
    username=request.data['username']
    password=request.data['password']

    if User.objects.filter(username=username):
        return Response(username + ' already exsist')

    User.objects.create_user(username=username, password=password)
    return Response(username + ' signup')

@api_view(['GET']) 
@renderer_classes([JSONRenderer]) 
def signin(request):
    username=request.data['username']
    password=request.data['password']

    current_user = request.user
    print( current_user)
    if username == current_user:
        return Response("already logged in")


    user = authenticate(username = username , password = password)

    if user is not None:
        login(request, user)
        return Response(username + " loged in")
    else:
        return Response("not a user")


@api_view(['GET']) 
@renderer_classes([JSONRenderer]) 
def signout(request):
    logout(request)
    return Response("sign out!")


