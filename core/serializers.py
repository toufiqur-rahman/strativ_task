from rest_framework import serializers

from core.models import Country, Language, Timezone


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['iso639_1', 'iso639_2', 'name', 'nativeName']


class TimezoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timezone
        fields = ['timezone']


class CountrySerializer(serializers.ModelSerializer):
    timezones = TimezoneSerializer(many=True, read_only=True)
    languages = LanguageSerializer(many=True, read_only=True)

    class Meta:
        model = Country
        fields = ['id', 'name', 'alphacode2', 'alphacode3', 'capital', 'population', 'flag', 'region', 'subregion',
                  'timezones', 'languages']

