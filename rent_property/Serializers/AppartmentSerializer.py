
from rest_framework import serializers
from rent_property.models import Apartment, ApartmentImages
from rent_property.Serializers.ApartmentImagesSerializer import ApartmentImagesSerializer


class ApartmentSerializer(serializers.ModelSerializer):
    apartment_images = serializers.SerializerMethodField('get_apartment_images')

    class Meta:
        model = Apartment
        fields = '__all__'

    def get_apartment_images(self, obj):
        serializer_context = {'request': self.context.get('request')}
        apartment_images_data = ApartmentImages.objects.filter(apartment=obj)
        serializer = ApartmentImagesSerializer(apartment_images_data, many=True, context=serializer_context)
        return serializer.data

    def create(self, validate_data):
        validated_data = self.initial_data
        apartment_images = validated_data.pop('apartment_images')
        apartment = Apartment.objects.create(**validated_data)

        for item in apartment_images:
            ApartmentImages.objects.create(apartment=apartment, **item)

        return apartment

    def update(self, instance, validate_data):
        validated_data = self.initial_data
        apartment_images = validated_data.pop('apartment_images')
        Apartment.objects.filter(id=instance.id).update(**validated_data)
        apartment = Apartment.objects.get(id=instance.id)

        for item in apartment_images:
            if "id" in item:
                ApartmentImages.objects.filter(id=item['id']).update(apartment=apartment, **item)
            else:
                ApartmentImages.objects.create(apartment=apartment, **item)

        return apartment
