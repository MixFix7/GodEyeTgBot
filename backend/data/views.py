from django.urls import path
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q

from . import models
from . import serializers


class AddPersonsData(APIView):
    def post(self, request):
        try:
            data = request.data.get('data')
            print(data)
            for person_data in data:
                # Розділіть дані на поля моделі
                name = person_data.get('name')
                phone_number = person_data.get('phone_number')
                ip = person_data.get('ip')
                organization = person_data.get('organization')
                location = person_data.get('location')
                city = person_data.get('city')
                emails = person_data.get('emails')
                social_data = person_data.get('social_data')[0]
                # Створіть об'єкт PersonData і збережіть його
                person_instance = models.PersonData(
                    name=name,
                    phone_number=phone_number,
                    ip=ip,
                    organization=organization,
                    location=location,
                    city=city,
                    emails=emails,
                )
                person_instance.save()

                if social_data:

                    instagram = social_data.get("instagram")
                    facebook = social_data.get("facebook")
                    tiktok = social_data.get("tiktok")
                    paypal = social_data.get("paypal")
                    twitter = social_data.get("twitter")
                    snapchat = social_data.get("snapchat")

                    social_data_person = models.SocialData(
                        person_id=person_instance.id,
                        instagram=instagram,
                        facebook=facebook,
                        tiktok=tiktok,
                        paypal=paypal,
                        twitter=twitter,
                        snapchat=snapchat,
                    ).save()

            return Response({'message': 'Persons were added successfully!'})

        except Exception as e:
            return Response({'message': str(e)})


class FindPerson(APIView):
    def post(self, request):
        data = request.data

        if not data:
            return Response({})

        filter_conditions = Q()

        valid_fields = [
            'name', 'phone_number', 'ip', 'organization', 'location',
            'city', 'emails'
        ]


        # Перебираємо всі ключі, що прийшли в запиті
        for field, value in data.items():
            if field in valid_fields:
                if field == 'name':
                    filter_conditions &= Q(**{f'{field}__icontains': value})
                else:
                    filter_conditions &= Q(**{field: value})

        results = models.PersonData.objects.filter(filter_conditions)
        result_json = serializers.PersonDataSerializer(results, many=True)

        return Response(result_json.data)

