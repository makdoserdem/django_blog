from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from uygulama import models


def blog(request):
    return HttpResponse('Yazılar burada')