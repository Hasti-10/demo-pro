from django.shortcuts import render

# Create your views here.
from djapp.models import *
from djapp.serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status
from rest_framework import generics
#from rest_framework import mixins
from rest_framework import filters
#from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class revlist(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backands = [filters.OrderingFilter,filters.SearchFilter]
    ordering_fields = ['result']
    search_fields =['^name',]


    def get_queryset(self):
        return Review.objects.order_by('product')
        return Review.objects.filter(result__gt=3)


class rev(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


"""class Reviewgeneric(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class mixin(mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = customer.objects.all()
    serializer_class = customerSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
"""


class pro(APIView):

    def get(self, request):
        p = Product.objects.all()
        serializer = ProductSerializer(p, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class pro_d(APIView):

    def get_obj(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except djapp.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        p = self.get_obj(pk)
        serializer = ProductSerializer(p)
        return Response(serializer.data)

    def put(self, request, pk):
        p = self.get_obj(pk)
        serializer = ProductSerializer(p, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        p = self.get_obj(pk)
        p.delete()
        return Response("error")


class cust(APIView):

    def get(self, request):
        p = customer.objects.all()
        serializer = customerSerializer(p, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = customerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class review(APIView):

    def get(self, request):
        p = Review.objects.all()
        serializer = ReviewSerializer(p, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
