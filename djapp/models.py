from django.db import models
from django.core.validators import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.

def alnum(value):
    if not str(value).isalnum():
        raise ValidationError("only numeric and alphabet value are allow.")
    return value


class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class customer(models.Model):
    cname = models.CharField(max_length=200)
    gam = models.CharField(max_length=100)
    date = models.DateField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="custnms", null=True)

    def __str__(self):
        return self.cname


class Review(models.Model):
    result = models.IntegerField(validators=[MaxValueValidator, MinValueValidator])
    comment = models.CharField(max_length=200,null=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE, related_name="Rewiews",null=True)
    creat = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "the rate of "+ self.product.name + "is " + str(self.result)
