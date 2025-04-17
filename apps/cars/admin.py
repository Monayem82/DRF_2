from django.contrib import admin

from apps.cars.models import CarModel,ShowroomModel,ReviewModel

class CarModelAdmin(admin.ModelAdmin):
    list_display=['id','model_no','name','descripe','price','showroom','create_at','updated_to']
    search_fields=['name','showroom']

admin.site.register(CarModel,CarModelAdmin)

class ShowroomModelAdmin(admin.ModelAdmin):
    list_display=['id','name','location','webside']
    search_fields=['name']
admin.site.register(ShowroomModel,ShowroomModelAdmin)

class ReviewModelAdmin(admin.ModelAdmin):
    list_display=['id','star','comments','car']
    search_fields=['star','car']

admin.site.register(ReviewModel,ReviewModelAdmin)

