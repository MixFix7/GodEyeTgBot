from rest_framework import serializers
from .models import *


class SocialDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialData
        fields = [
            'instagram', 'facebook',
            'tiktok', 'paypal',
            'twitter', 'snapchat',
        ]


class PersonDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonData
        fields = [
            'name', 'phone_number', 'ip',
            'organization', 'location', 'city', 'emails',
        ]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        social_data = instance.social_data
        data['social_data'] = SocialDataSerializer(social_data, many=True).data
        return data

