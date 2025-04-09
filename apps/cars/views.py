from django.shortcuts import render,HttpResponse,Http404
from apps.cars.models import CarModel,ShowroomModel,ReviewModel

from apps.cars.serializers import CarModelSerializer,ShowroomSerializer,ReviewSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view,APIView

from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly


class ReviewApiview(APIView):
    def get(self,request):
        showroom=ReviewModel.objects.all()
        serializer=ReviewSerializer(showroom,many=True,context={'request': request})
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer=ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



class ShowroomApiView(APIView):
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]

    def get(self,request):
        showroom=ShowroomModel.objects.all()
        serializer=ShowroomSerializer(showroom,many=True,context={'request': request})
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer=ShowroomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class ShowroomApiDetailsView(APIView):
    def get_object(self,pk):
        try:
            showroom=ShowroomModel.objects.get(pk=pk)
            return showroom
        except ShowroomModel.DoesNotExist:
            raise Http404
        
    def get(self,request,pk):
        showroom=self.get_object(pk=pk)
        serializer=ShowroomSerializer(showroom)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,pk):
        showroom=self.get_object(pk=pk)
        serializer=ShowroomSerializer(showroom,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,pk):
        showroom=self.get_object(pk=pk)
        showroom.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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
    def get_objects(self,pk):
        try:
            car=CarModel.objects.get(pk=pk)
            return car
        except CarModel.DoesNotExist:
            raise Http404
    def get(self,request,pk):
        car=self.get_objects(pk=pk)
        serializer=CarModelSerializer(car)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,pk):
        car=self.get_objects(pk=pk)
        serializer=CarModelSerializer(car,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,pk):
        car=self.get_objects(pk=pk)
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
