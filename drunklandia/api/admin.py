from django.contrib import admin
from drunklandia.api import models

# Register your models here.
admin.site.register(models.Restaurant)
admin.site.register(models.Address)
admin.site.register(models.RestaurantHours)
admin.site.register(models.Special)
admin.site.register(models.SpecialHours)
admin.site.register(models.Amenity)
admin.site.register(models.RestaurantAmenities)
admin.site.register(models.Review)