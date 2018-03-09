"""drunklandia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.conf.urls import url, include
from rest_framework import routers
from drunklandia.api import views
from rest_framework_swagger.views import get_swagger_view

router = routers.DefaultRouter()

router.register(r'restaurant', views.RestaurantViewSet)
router.register(r'address', views.AddressViewSet)
router.register(r'restaurant_hours', views.RestaurantHoursViewSet)
router.register(r'specials', views.SpecialViewSet)
router.register(r'special_hours', views.SpecialHoursViewSet)
router.register(r'amenities', views.AmenityViewSet)
router.register(r'restaurant_amenities', views.RestaurantAmenitiesViewSet)
router.register(r'reviews', views.ReviewViewSet)

schema_view = get_swagger_view(title='Drunklandia API')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', schema_view),
    url(r'^api/v1/', include(router.urls)),
    url(r'^api/v1/auth/', include('djoser.urls')),
    url(r'^api/v1/auth/', include('djoser.urls.jwt')),
]