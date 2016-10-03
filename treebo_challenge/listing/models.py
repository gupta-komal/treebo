from django.db import models

# Create your models here.


class Hotel_Deals(models.Model):

    name = models.CharField(null=True, blank=True, max_length=500)
    image = models.CharField(null=True, blank=True, max_length=500)
    rating = models.FloatField(null=True, blank=True, max_length=10)
    link = models.CharField(null=True, blank=True, max_length=500)
    actual_price = models.CharField(null=True, blank=True, max_length=100000)
    discount = models.CharField(null=True, blank=True, max_length=1000)
    location = models.CharField(null=True, blank=True, max_length=1000)

    def __str__(self):
        return self.name

    def final_price(self):
        if self.discount:
            discount = int(self.discount)
        else:
            discount = 0
        final_price = int(self.actual_price) - ((int(self.actual_price) * discount)/100)
        return round(final_price)

    def city(self):
        location = self.location.split(',')
        length = len(location)-2
        return location[length]

    def rating_star(self):
        if 4 < self.rating <= 5:
            return 5
        elif 3 < self.rating <= 4:
            return 4
        elif 2 < self.rating <= 3:
            return 3
        elif 1 < self.rating <= 2:
            return 2
        elif 0 < self.rating <= 1:
            return 1
        else:
            return 0