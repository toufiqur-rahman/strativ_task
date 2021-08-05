import requests
from django.core.management.base import BaseCommand, CommandError

from core.helpers import get_country_api_data
from core.models import Country, Language, Timezone


class Command(BaseCommand):
    def handle(self, *args, **options):
        Language.objects.all().delete()
        Timezone.objects.all().delete()
        Country.objects.all().delete()

        countries = get_country_api_data()
        for country in countries:
            _obj = {
                'name': country['name'],
                'alphacode2': country['alpha2Code'],
                'alphacode3': country['alpha3Code'],
                'capital': country['capital'],
                'population': country['population'],
                'flag': country['flag'],
                'region': country['region'],
                'subregion': country['subregion']
            }

            _country_obj = Country.objects.create(**_obj)
            for language in country['languages']:
                print(language)
                _lang_obj = {
                    'iso639_1': language['iso639_1'],
                    'iso639_2': language['iso639_2'],
                    'name': language['name'],
                    'nativeName': language['nativeName'],
                    'country': _country_obj
                }
                Language.objects.create(**_lang_obj)

            for timezone in country['timezones']:
                Timezone.objects.create(timezone=timezone, country=_country_obj)

        self.stdout.write(self.style.SUCCESS('Data saved successfuly'))