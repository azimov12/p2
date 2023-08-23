from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse
# Create your views here.

def boots(request):
    return HttpResponse('This is place of boots')

def t_shirts(request):
    return HttpResponse('This is place of T shirts')    

def balls(request):
    return HttpResponse('This is place of different balls')