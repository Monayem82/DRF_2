from django.shortcuts import render,HttpResponse
from apps.user_app.serializers import RegistrationSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET','POST'])
def Registration_view(request):
    if request.method=="POST":
        serializer=RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    return Response({'Register Api':'Developer time'})
