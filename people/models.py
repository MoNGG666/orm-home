from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=255)


class City(models.Model):
    name = models.CharField(max_length=255)
    country = models.ForeignKey(
        'people.Country',
        null=True,
        on_delete=models.CASCADE,
        related_name='cities',
    )



class Citizen(models.Model):
    full_name = models.CharField(max_length=255)
    city = models.ForeignKey(
        'people.City',
        null=True,
        on_delete=models.CASCADE,
        related_name='citizens',
    )
