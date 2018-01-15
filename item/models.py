from django.db import models
from django.utils import timezone

class Item(models.Model):
    title = models.CharField(max_length=300)
    comment = models.TextField(blank=True, null=True)
    unit_cost = models.FloatField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    total_cost = models.FloatField(blank=True, null=True)

    def get_total_cost(self):
        self.total_cost = self.unit_cost * self.quantity
        self.save()

    def set_unit_cost(self,cost):
        self.unit_cost = cost
        self.save()

    def set_quantity(self,quantity):
        self.quantity = quantity
        self.save()

    def __str__(self):
        return self.title

