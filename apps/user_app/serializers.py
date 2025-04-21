from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError

class RegistrationSerializer(serializers.ModelSerializer):
    password_confirmation=serializers.CharField(style={'input_type':'password'},write_only=True)

    class Meta:
        model=User
        fields=['username','email','password','password_confirmation']
        extra_kwargs={
            'password':{'write_only':True},
            #'password_confirmaton':{'write_only':True},
        }

    def save(self):
        user_name=self.validated_data['username']
        val_email=self.validated_data['email']
        password=self.validated_data['password']
        password_confirmation=self.validated_data['password_confirmation']

        if password !=password_confirmation:
            raise serializers.ValidationError({'Error':'Password Dont match'})
        
        
        if User.objects.filter(email=val_email).exists():
            raise serializers.ValidationError({'Error':'Email already use'})
        
        account=User(username=user_name,email=val_email)
        account.set_password(password)
        account.save()
        return account