import json

from django.shortcuts import render
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import Country, Language
from core.serializers import CountrySerializer


class CountryListAPIView(APIView):
    def get(self, request):
        country_list = CountrySerializer(Country.objects.all(), many=True)
        serializer = CountrySerializer(country_list)
        return Response(serializer.data)


class CountryAPIView(APIView):
    def get(self, request, pk):
        country = Country.objects.filter(pk=pk).last()
        serializer = CountrySerializer(country)
        return Response(serializer.data)


class CountryCreateAPIView(APIView):
    def post(self, request):
        serializer = CountrySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)


class CountryUpdateAPIView(APIView):
    def post(self, request, pk):
        country_update = Country.objects.filter(pk=pk).last()
        serializer = CountrySerializer(instance=country_update, data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)


class CountryDeleteAPIView(APIView):
    def delete(self, request, pk):
        country_delete = Country.objects.filter(pk=pk).last()
        country_delete.delete()
        msg = {"testing message":'country deleted'}
        return Response(msg)


class SameLanguageCountryAPIView(APIView):
    def get(self, request):
        language = request.GET.get('language', None)
        if language:
            # Language.objects.filter(name=language)
            countries = Country.objects.filter(languages__name__icontains=language)
            serializer = CountrySerializer(countries, many=True)
            return Response(serializer.data)
        return Response({'status': False, 'message': 'Please specify a language'})


class SearchCountryByNameAPIView(APIView):
    def get(self, request):
        country_name = request.GET.get('name', None)
        if country_name:
            countries = Country.objects.filter(name__icontains=country_name)
            serializer = CountrySerializer(countries, many=True)
            return Response(serializer.data)
        return Response({'status': False, 'message': 'Please specify a language'})


class CountryListView(View):
    def get(self, request):
        countries = Country.objects.all()
        context = {'countries': countries}
        return render(request, 'core/country_list.html', context)

