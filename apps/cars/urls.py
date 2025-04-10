from django.urls import path
from apps.cars import views

urlpatterns = [
    #path('',views.CarViews,name="carViews"),

    #Function based url
    #path('api/',views.carApiView),
    #path('api/<int:pk>',views.carDetailsView),

    #Class based urls setup

    path('review/api/',views.ReviewApiview.as_view(),name="reviews"),
    path('review/api/<int:pk>',views.ReviewDetailsView.as_view(),name="review"),

    path('showroom/api/',views.ShowroomApiView.as_view(),name="showroomApi"),
    path('showroom/api/<int:pk>',views.ShowroomApiDetailsView.as_view(),name="showroomApiDetails"),
    
    path('api/',views.carApiView.as_view(),name="car_list"),
    path('api/<int:pk>',views.carApiDetailsView.as_view(),name="car_details_view")
]
