from django.shortcuts import render
from rest_framework.views import APIView
from . import models
from . import serializers
from rest_framework.response import Response


class AddPersonsData(APIView):
    def post(self, request):
        try:
            for person_data in request.data:
                person = serializers.PersonData(data=person_data)

                if person.is_valid():
                    person.save()

            return Response({'message': 'Persons was added successfully!'})

        except Exception as e:
            return Response({'message': str(e)})


class FindPerson(APIView):
    def post(self, request):
        try:
            data = request.data
            filter_kwargs = {}

            for key, value in data.items():
                if value is not None:
                    filter_kwargs[key] = value
                else:
                    filter_kwargs[f'{key}__isnull'] = True

            result = models.PersonData.filter(**filter_kwargs)
            result_json = serializers.PersonData(result, many=True)

            return Response(result_json)

        except Exception as e:
            return Response({'message': str(e)})


