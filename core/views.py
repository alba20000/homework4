from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.


def index(request):
    return HttpResponse("Hello!")


def timedate(request):
    current_time = datetime.datetime.now()
    return HttpResponse(current_time.strftime("%d %b %Y %H:%M:%S"))
