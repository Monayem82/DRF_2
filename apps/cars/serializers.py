from rest_framework import serializers

from apps.cars.models import CarModel

class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = "__all__"

    def validate_price(self, value):
        if value<= 200000.00:
            raise serializers.ValidationError('Price is more then 200000.00')
        return value
    
    def validate(self, data):
        if data['name'] == data['model_no']:
            raise serializers.ValidationError("Error : name and Model_no Must be deffirent")
        return data