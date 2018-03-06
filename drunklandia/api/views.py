from rest_framework import viewsets, filters
from drunklandia.api import serializers, models


class TestModelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.TestModel.objects.all()
    serializer_class = serializers.TestModelSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = '__all__'