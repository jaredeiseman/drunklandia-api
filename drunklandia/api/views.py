from rest_framework import viewsets, filters
from drunklandia.api import serializers, models


class RestaurantViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.Restaurant.objects.all()
    serializer_class = serializers.RestaurantSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = '__all__'


class AddressViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.Address.objects.all()
    serializer_class = serializers.AddressSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = '__all__'


class RestaurantHoursViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.RestaurantHours.objects.all()
    serializer_class = serializers.RestaurantHoursSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = '__all__'


class SpecialViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.Special.objects.all()
    serializer_class = serializers.SpecialSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = '__all__'


class SpecialHoursViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.SpecialHours.objects.all()
    serializer_class = serializers.SpecialHoursSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = '__all__'


class AmenityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.Amenity.objects.all()
    serializer_class = serializers.AmenitySerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = '__all__'


class RestaurantAmenitiesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.RestaurantAmenities.objects.all()
    serializer_class = serializers.RestaurantAmenitiesSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = '__all__'


class ReviewViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = '__all__'
