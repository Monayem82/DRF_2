from django.urls import path
from apps.cars import views

urlpatterns = [
    #path('',views.CarViews,name="carViews"),

    #Function based url
    #path('api/',views.carApiView),
    #path('api/<int:pk>',views.carDetailsView),


    #Class based urls setup
    path('api/',views.carApiView.as_view()),
    path('api/<int:pk>',views.carApiDetailsView.as_view())
]
