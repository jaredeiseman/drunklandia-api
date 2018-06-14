from rest_framework import viewsets, filters
from rest_framework.views import APIView
from drunklandia.api import serializers, models
from drunklandia import permissions
import django_filters.rest_framework
from rest_framework.response import Response
from rest_framework_jwt.utils import jwt_decode_handler


class RestaurantViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Restaurant object
    """
    queryset = models.Restaurant.objects.all()
    serializer_class = serializers.RestaurantSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = '__all__'
    # permission_classes = (permissions.IsOwnerOrReadOnly,)


class RestaurantHoursViewSet(viewsets.ModelViewSet):
    """
    API endpoint for RestaurantHours object
    """
    queryset = models.RestaurantHours.objects.all()
    serializer_class = serializers.RestaurantHoursSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = '__all__'


class SpecialViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Special object
    """
    queryset = models.Special.objects.all()
    serializer_class = serializers.SpecialSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = '__all__'


class SpecialHoursViewSet(viewsets.ModelViewSet):
    """
    API endpoint for SpecialHours object
    """
    queryset = models.SpecialHours.objects.all()
    serializer_class = serializers.SpecialHoursSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = '__all__'


class AmenityViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Amenity object
    """
    queryset = models.Amenity.objects.all()
    serializer_class = serializers.AmenitySerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = '__all__'


class RestaurantAmenitiesViewSet(viewsets.ModelViewSet):
    """
    API endpoint for RestaurantAmenities union object
    """
    queryset = models.RestaurantAmenities.objects.all()
    serializer_class = serializers.RestaurantAmenitiesSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_fields = ('restaurant_id',)
    ordering_fields = '__all__'


class ProflieViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Profile object
    """
    queryset = models.Profile.objects.all()
    serializer_class = serializers.ProfileSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_fields = ('user',)
    ordering_fields = '__all__'

class Favorites(APIView):
    def get(self, request, format=None):
        token = request.META['HTTP_AUTHORIZATION'][4:]
        user_id = jwt_decode_handler(token)['user_id']
        profile = models.Profile.objects.get(user=user_id)
        return Response(profile.favorites)

    def patch(self, request, format=None):
        token = request.META['HTTP_AUTHORIZATION'][4:]
        user_id = jwt_decode_handler(token)['user_id']
        profile = models.Profile.objects.get(user=user_id)
        profile.favorites = request.data['favorites']
        profile.save()
        return Response(profile.favorites)
    