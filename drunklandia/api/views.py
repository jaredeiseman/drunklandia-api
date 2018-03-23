from rest_framework import viewsets, filters
from drunklandia.api import serializers, models
from drunklandia import permissions


class RestaurantViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Restaurant object
    """
    queryset = models.Restaurant.objects.all()
    serializer_class = serializers.RestaurantSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = '__all__'
    permission_classes = (permissions.IsOwnerOrReadOnly,)


class AddressViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Address object
    """
    queryset = models.Address.objects.all()
    serializer_class = serializers.AddressSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = '__all__'


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
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = '__all__'


class ReviewViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Review object
    """
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = '__all__'
