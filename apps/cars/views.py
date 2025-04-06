from django.shortcuts import render,HttpResponse

from apps.cars.serializers import CarModelSerializer
from rest_framework.response import Response
from rest_framework import status

def CarViews(request):
    return HttpResponse("<p>This is the tour </p>")


#Function based view

