from django.db import models

# Create your models here.
class TestModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    test_prop = models.CharField(max_length=255)