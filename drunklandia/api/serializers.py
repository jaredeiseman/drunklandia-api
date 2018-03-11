from rest_framework import serializers
from drunklandia.api.models import *


class AddressSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Address
        fields = '__all__'


class RestaurantHoursSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = RestaurantHours
        fields = '__all__'


class SpecialHoursSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SpecialHours
        fields = '__all__'


class SpecialSerializer(serializers.ModelSerializer):
    special_hours = SpecialHoursSerializer(many=True)
    
    class Meta:
        model = Special
        fields = '__all__'


class AmenitySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Amenity
        fields = '__all__'

from pprint import pprint
class RestaurantAmenitiesSerializer(serializers.ModelSerializer):
    amenity = serializers.SerializerMethodField()

    def get_amenity(self, obj):
        query_set = Amenity.objects.all().filter(amenity=obj.amenity_id)
        return [AmenitySerializer(m).data for m in query_set]
    
    class Meta:
        model = RestaurantAmenities
        fields = ('amenity',)


class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = '__all__'


class RestaurantSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    restaurant_hours = RestaurantHoursSerializer(many=True)
    specials = SpecialSerializer(many=True)
    amenities = RestaurantAmenitiesSerializer(many=True)
    restaurant_reviews = ReviewSerializer(many=True)

    class Meta:
        model = Restaurant
        fields = ('created', 'name', 'phone', 'address', 'restaurant_hours', 'specials', 'amenities', 'restaurant_reviews',)
        depth = 3