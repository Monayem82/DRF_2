from django.urls import path
from apps.cars import views

urlpatterns = [
    #path('',views.CarViews,name="carViews"),

    path('api/',views.carApiView),
    path('api/<int:pk>',views.carDetailsView),
]
