from rest_framework import serializers

from apps.cars.models import CarModel,ShowroomModel


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
    

class ShowroomSerializer(serializers.ModelSerializer):
    #showrooms=CarModelSerializer(many=True,read_only=True)
    #showrooms= serializers.StringRelatedField(many=True) #model a str function a je fields deya setai dibe
    #showrooms=serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    # showrooms = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='car_details_view'
    # )

    showrooms = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='descripe'
     )
    
    class Meta:
        model=ShowroomModel
        fields="__all__"
