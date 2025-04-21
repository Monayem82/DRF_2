from django.shortcuts import render,HttpResponse
from apps.user_app.serializers import RegistrationSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,authentication_classes
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.tokens import RefreshToken

@api_view(['POST',])
@authentication_classes([TokenAuthentication])
def DeleteUserToken(request):
    if request.method=='POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


@api_view(['GET','POST'])
def Registration_view(request):
    if request.method=="POST":
        serializer=RegistrationSerializer(data=request.data)
        data={}
        if serializer.is_valid():
            account=serializer.save()

            data['username']=account.username
            data['email']=account.email
            data['hi']=account.email

            # token,_=Token.objects.get_or_create(user=account)
            # data['token']=token.key
            refresh = RefreshToken.for_user(account)
            data['token']={
                            'refresh': str(refresh),
                            'access': str(refresh.access_token),
                        }
            
            return Response(data)

            #return Response(serializer.data)
        else:
            return Response(serializer.errors)
    return Response({'Register Api':'Developer time'})
