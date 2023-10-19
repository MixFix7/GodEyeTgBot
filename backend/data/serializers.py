from rest_framework import serializers
from .models import *


class SocialDataSerializer(serializers):
    class Meta:
        model = SocialData
        fields = '__all__'


class PersonDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonData
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        social_data = instance.social_data
        data['social_data'] = SocialDataSerializer(social_data)

