from django.urls import path
from apps.user_app import views

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns =[
    path('login/',obtain_auth_token,name="login"),
    path('register/',views.Registration_view,name='register'),
    path('logout/',views.DeleteUserToken,name='logout'),
]
