from rest_framework import serializers
from djapp.models import *
from django.core.validators import ValidationError


class ProductSerializer(serializers.ModelSerializer):
    discount = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_discount(self, obj):
        dispric = obj.price - 1000
        return dispric

    def validate_price(self, value):
        if value > 5000:
            raise serializers.ValidationError("price must be less then 5000.")
        return value

    def __str__(self):
        return self.name


class customerSerializer(serializers.ModelSerializer):
    custnms = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = customer
        fields = '__all__'

    def __str__(self):
        return self.cname


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['result','comment','product']