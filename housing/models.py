from django.db import models
from django.utils.html import mark_safe


class Selling(models.Model):
    customer = models.CharField(max_length=100)
    price = models.IntegerField()
    house_type = models.CharField(max_length=75)
    image = models.ImageField(null=True,default='defaulthouse.jpg')


    def img_preview(self): 
        return mark_safe(f'<img src = "{self.image}" width = "80" height="80" />')

                         



    def __str__(self) -> str:
        return self.customer

