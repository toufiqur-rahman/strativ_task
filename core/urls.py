from django.urls import path

from core.views import CountryListAPIView, CountryAPIView, CountryCreateAPIView, SameLanguageCountryAPIView, \
    SearchCountryByNameAPIView, CountryListView, CountryUpdateAPIView, CountryDeleteAPIView

urlpatterns = [
    path('countries/', CountryListAPIView.as_view()),
    path('countries/<int:pk>/', CountryAPIView.as_view()),
    path('countries/create/', CountryCreateAPIView.as_view()),
    path('countries/update/<int:pk>', CountryUpdateAPIView.as_view()),
    path('countries/delete/<int:pk>', CountryDeleteAPIView.as_view()),
    path('countries/same-language/', SameLanguageCountryAPIView.as_view()),
    path('countries/search-country/', SearchCountryByNameAPIView.as_view()),
    path('templates/countries/', CountryListView.as_view()),
]