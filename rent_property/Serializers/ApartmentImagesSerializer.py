
from rest_framework import serializers
from rent_property.models import ApartmentImages


class ApartmentImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApartmentImages
        fields = '__all__'

    def create(self, validate_data):
        validated_data = self.initial_data
        apartment = validated_data.pop('apartment', None)
        instance = ApartmentImages.objects.create(apartment_id=apartment, **validated_data)
        return instance

    def update(self, instance, validate_data):
        validated_data = self.initial_data
        apartment = validated_data.pop('apartment', None)
        ApartmentImages.objects.filter(id=instance.id).update(apartment_id=apartment, **validated_data)
        instance = ApartmentImages.objects.get(id=instance.id)

        return instance
