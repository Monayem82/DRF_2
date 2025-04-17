from django.urls import path,include
from apps.cars import views
from rest_framework.routers import DefaultRouter



router=DefaultRouter()
router.register(r'api',views.CarApiViewsets,basename='users')

urlpatterns = [
    #path('',views.CarViews,name="carViews"),

    #Function based url
    #path('api/',views.carApiView),
    #path('api/<int:pk>',views.carDetailsView),

    #Class based urls setup

    path('review/api/',views.ReviewApiview.as_view(),name="reviews"),
    path('review/api/<int:pk>',views.ReviewDetailsView.as_view(),name="review"),

    path('showroom/<int:pk>/review/',views.ReviewsListView.as_view(),name="review_list")

    path('showroom/api/',views.ShowroomApiView.as_view(),name="showroomApi"),
    path('showroom/api/<int:pk>',views.ShowroomApiDetailsView.as_view(),name="showroomApiDetails"),
    
    # Viewsets in car Model
    path('viewset/',include(router.urls)),

    # path('api/',views.carApiView.as_view(),name="car_list"),
    # path('api/<int:pk>',views.carApiDetailsView.as_view(),name="car_details_view")
]

#urlpatterns +=urlpatterns+ router.urls