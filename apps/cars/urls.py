from django.urls import path
from apps.cars import views

urlpatterns = [
    path('',views.CarViews,name="carViews"),
]
