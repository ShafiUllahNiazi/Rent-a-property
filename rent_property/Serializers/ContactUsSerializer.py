
from rest_framework import serializers
from rent_property.models import ContactUs


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = '__all__'

    def create(self, validated_data):
        validated_data = self.initial_data
        instance = ContactUs.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        validated_data = self.initial_data
        instance = ContactUs.objects.filter(id=instance.id).update(**validated_data)
        return instance
