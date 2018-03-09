from rest_framework import serializers
from drunklandia.api.models import *

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class RestaurantHoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantHours
        fields = '__all__'

class SpecialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Special
        fields = '__all__'

class SpecialHoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialHours
        fields = '__all__'

class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields = '__all__'

class RestaurantAmenitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantAmenities
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

