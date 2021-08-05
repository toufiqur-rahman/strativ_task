from django.db import models


class Timezone(models.Model):
    timezone = models.CharField(max_length=12)
    country = models.ForeignKey('core.Country', on_delete=models.DO_NOTHING, related_name='timezones')

    def __str__(self):
        return self.timezone


class Language(models.Model):
    iso639_1 = models.CharField(max_length=2, null=True)
    iso639_2 = models.CharField(max_length=3)
    name = models.CharField(max_length=100)
    nativeName = models.CharField(max_length=100)
    country = models.ForeignKey('core.Country', on_delete=models.DO_NOTHING, related_name='languages')

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=100)
    alphacode2 = models.CharField(max_length=2)
    alphacode3 = models.CharField(max_length=3)
    capital = models.CharField(max_length=100)
    population = models.IntegerField()
    flag = models.URLField(max_length=255)
    region = models.CharField(max_length=100)
    subregion = models.CharField(max_length=100)
    neighbours = models.ManyToManyField('self')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']