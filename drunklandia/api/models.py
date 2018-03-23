from django.db import models
from django.contrib.auth.models import User
from drunklandia.api import utils


class Restaurant(models.Model):
    """
    restaurant: id, created, created_by, name, phone
    """
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, models.DO_NOTHING, null=True, blank=True)
    name = models.CharField(max_length=255, blank=False, null=False)
    phone = models.DecimalField(null=False, blank=False, decimal_places=0, max_digits=10)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'Restaurant'


class Address(models.Model):
    """
    Address: id, created, created_by, street_one, street_two, city, state, zip, lat, lng, restaurant_id
    """
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, models.DO_NOTHING, null=True, blank=True)
    street_one = models.CharField(max_length=255, blank=False, null=False)
    street_two = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=False, null=False)
    state = models.CharField(max_length=2, blank=False, null=False)
    zip_code = models.DecimalField(decimal_places=0, max_digits=5, null=False, blank=False)
    lat = models.DecimalField(decimal_places=10, max_digits=32, null=False, blank=False)
    lng = models.DecimalField(decimal_places=10, max_digits=32, null=False, blank=False)
    restaurant_id = models.OneToOneField(Restaurant, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.street_one

    class Meta:
        db_table = 'Address'


class RestaurantHours(models.Model):
    """
    restaurant_hours: id, created, created_by, day (int), open, close, restaurant_id (FK)
    """
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, models.DO_NOTHING, null=True, blank=True)
    restaurant_id = models.ForeignKey(Restaurant, models.DO_NOTHING, null=False, blank=False, related_name='restaurant_hours')
    day = models.IntegerField(choices=utils.DAY_CHOICES, null=False, blank=False)
    open_time = models.TimeField(blank=False, null=False)
    close_time = models.TimeField(blank=False, null=False)

    class Meta:
        db_table = 'RestaurantHours'


class Special(models.Model):
    """
    special: id, created, created_by, restaurant_id, description, price
    """
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, models.DO_NOTHING, null=True, blank=True)
    restaurant_id = models.ForeignKey(Restaurant, models.DO_NOTHING, null=False, blank=False, related_name='specials')
    description = models.TextField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=3, decimal_places=2, null=False, blank=False)
    
    class Meta:
        db_table = 'Special'


class SpecialHours(models.Model):
    """
    special_hours: id, created, created_by, day (int), start_time, stop_time, special_id, restaurant_id
    """
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, models.DO_NOTHING, null=True, blank=True)
    restaurant_id = models.ForeignKey(Restaurant, models.DO_NOTHING, null=False, blank=False)
    special_id = models.ForeignKey(Special, models.DO_NOTHING, null=False, blank=False, related_name='special_hours')
    start_time = models.TimeField(blank=False, null=False)
    stop_time = models.TimeField(blank=False, null=False)
    day = models.IntegerField(choices=utils.DAY_CHOICES, null=False, blank=False)

    class Meta:
        db_table = 'SpecialHours'


class Amenity(models.Model):
    """
    amenity: id, created, created_by, amenity
    """
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, models.DO_NOTHING, null=True, blank=True)
    amenity = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.amenity

    class Meta:
        db_table = 'Amenity'


class RestaurantAmenities(models.Model):
    """
    m2m junction table
    RestaurantAmenity: id, restaurant_id, amenity_id
    """
    restaurant_id = models.ForeignKey(Restaurant, models.DO_NOTHING, null=False, blank=False, related_name='amenities')
    amenity_id = models.ForeignKey(Amenity, models.DO_NOTHING, null=False, blank=False)
    
    class Meta:
        db_table = 'RestaurantAmenities'


class Review(models.Model):
    """
    review: id, created, created_by, restaurant_id, rating, review
    """
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, models.DO_NOTHING, null=True, blank=True)
    restaurant_id = models.ForeignKey(Restaurant, models.DO_NOTHING, null=False, blank=False, related_name='restaurant_reviews')
    rating = models.IntegerField(null=False, blank=False, choices=utils.RATING_CHOICES)
    review = models.TextField(max_length=500, null=False, blank=False)

    class Meta:
        db_table = 'Review'