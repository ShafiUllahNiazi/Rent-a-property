
from django.db import models


class Apartment(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    apartment_type = models.CharField(max_length=200, null=True, blank=True)
    property_status = models.CharField(max_length=200, null=True, blank=True)
    no_of_rooms = models.IntegerField(default=0, blank=True, null=True)
    no_of_washrooms = models.IntegerField(default=0, blank=True, null=True)
    area = models.CharField(max_length=200, null=True, blank=True)
    address = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.CharField(max_length=200, null=True, blank=True)
    Latitude=models.CharField(max_length=200, null=True, blank=True)
    Longitude=models.CharField(max_length=200, null=True, blank=True)

class ApartmentImages(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, related_name="apartment_images")
    pictures = models.TextField(blank=True, null=True)


class ContactUs(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    message = models.TextField(blank=True, null=True)
