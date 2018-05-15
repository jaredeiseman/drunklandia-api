from rest_framework import serializers
from drunklandia.api.models import *


class RestaurantHoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantHours
        fields = '__all__'


class SpecialHoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialHours
        fields = '__all__'


class SpecialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Special
        fields = '__all__'


class AmenitySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Amenity
        fields = '__all__'


class RestaurantAmenitiesSerializer(serializers.ModelSerializer):
    amenity_details = AmenitySerializer()
    class Meta:
        model = RestaurantAmenities
        fields = ('restaurant_id', 'amenity_details',)
        # depth = 1 # TODO: this isnt right... need to do depth 1 on only the amenities


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'