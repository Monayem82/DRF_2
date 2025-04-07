from django.contrib import admin

from apps.cars.models import CarModel,ShowroomModel

class CarModelAdmin(admin.ModelAdmin):
    list_display=['id','model_no','name','descripe','price','create_at','updated_to']
    search_fields=['name']

admin.site.register(CarModel,CarModelAdmin)

class ShowroomModelAdmin(admin.ModelAdmin):
    list_display=['id','name','location','webside']
    search_fields=['name']
admin.site.register(ShowroomModel,ShowroomModelAdmin)

