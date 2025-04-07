from rest_framework import serializers

from apps.cars.models import CarModel

class CarModelSerializer(serializers.ModelSerializer):
    discounted_price=serializers.SerializerMethodField()
    class Meta:
        model = CarModel
        fields = "__all__"

    def get_discounted_price(self,object):#model ar sb filed object ar madhome asbe and use korte parbo object ar moto kore
        if object.price>200000:
            discount=object.price - 150000
            return discount

    #Field-level Validate
    def validate_price(self, value):
        if value<= 200000.00:
            raise serializers.ValidationError('Price is more then 200000.00')
        return value
    # Object level validate 
    def validate(self, data): # here data is the object in the above model
        if data['name'] == data['model_no']:
            raise serializers.ValidationError("Error : name and Model_no Must be deffirent")
        return data