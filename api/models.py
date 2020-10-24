from django.db import models

class Country(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.code + ":" + self.name

class State(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name
