from django.db import models as _models


class Site(_models.Model):
    """Site model"""
    name = _models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Value(_models.Model):
    """Value model"""
    site = _models.ForeignKey(Site, on_delete=_models.CASCADE)
    date = _models.DateField()
    a = _models.DecimalField('Value A', max_digits=7, decimal_places=2)
    b = _models.DecimalField('Value B', max_digits=7, decimal_places=2)

    def __str__(self):
        return f'[{self.date}] A: {self.a}, B: {self.b}'

