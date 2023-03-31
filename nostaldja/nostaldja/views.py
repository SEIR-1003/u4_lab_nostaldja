from django.shortcuts import render
from .models import Decade, Fads
from rest_framework import generics
from .serializers import DecadeSerializer, FadsSerializer

# Create your views here.


class DecadeList(generics.ListCreateAPIView):
    queryset = Decade.objects.all()
    serializer_class = DecadeSerializer


class DecadeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Decade.objects.all()
    serializer_class = DecadeSerializer


class FadsList(generics.ListCreateAPIView):
    queryset = Fads.objects.all()
    serializer_class = FadsSerializer


class FadsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fads.objects.all()
    serializer_class = FadsSerializer
