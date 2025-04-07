from django.contrib import admin

from apps.cars.models import CarModel

class CarModelAdmin(admin.ModelAdmin):
    list_display=['id','model_no','name','descripe','price','create_at','updated_to']

admin.site.register(CarModel,CarModelAdmin)
