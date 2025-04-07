from django.shortcuts import render,HttpResponse
from apps.cars.models import CarModel

from apps.cars.serializers import CarModelSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view,APIView

# def CarViews(request):
#     return HttpResponse("<p>This is the tour </p>")


#Function based view
# @api_view(['GET','POST'])
# def carApiView(request):
#     if request.method=="GET":
#         cars=CarModel.objects.all()
#         serializer=CarModelSerializer(cars,many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)
    
#     elif request.method=="POST":
#         serializer=CarModelSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

# @api_view(['GET','PUT','DELETE'])
# def carDetailsView(request,pk):
#     try:
#         car=CarModel.objects.get(pk=pk)
#     except:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method=="GET":
#         serializer=CarModelSerializer(car)
#         return Response(serializer.data,status=status.HTTP_200_OK)
    
#     elif request.method=="PUT":
#         serializer=CarModelSerializer(car,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
#     elif request.method=="DELETE":
#         car.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    

#Class based Views

class carApiView(APIView):
    def get(self,request):
        car=CarModel.objects.all()
        serializer=CarModelSerializer(car,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer=CarModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
class carApiDetailsView(APIView):
    def get(self,request,pk):
        car=CarModel.objects.get(pk=pk)
        serializer=CarModelSerializer(car)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,pk):
        car=CarModel.objects.get(pk=pk)
        serializer=CarModelSerializer(car,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,pk):
        car=CarModel.objects.get(pk=pk)
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)