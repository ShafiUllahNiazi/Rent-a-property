
from django.db import models


class Apartment(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    apartment_type = models.CharField(max_length=200, null=True, blank=True)
    property_status = models.CharField(max_length=200, null=True, blank=True)
    no_of_rooms = models.CharField(max_length=200, null=True, blank=True)
    no_of_washrooms = models.CharField(max_length=200, null=True, blank=True)
    #area_unit = models.CharField(max_length=200, null=True, blank=True)
    area = models.CharField(max_length=200, null=True, blank=True)
    # address = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.CharField(max_length=200, null=True, blank=True)
    latitude = models.CharField(max_length=200, null=True, blank=True)
    longitude = models.CharField(max_length=200, null=True, blank=True)
    state = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    street_address = models.TextField(blank=True, null=True)


class ApartmentImages(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, related_name="apartment_images")
    pictures = models.TextField(blank=True, null=True)


class ContactUs(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    message = models.TextField(blank=True, null=True)
