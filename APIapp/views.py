from django.shortcuts import render
from rest_framework import viewsets
from .serializers import DownExpSerializer, UpExpSerializer, AnnotationSerializer
from .models import DownExp, UpExp, Annotations
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.


class DownExpViewset(viewsets.ModelViewSet):
    serializer_class = DownExpSerializer
    queryset = DownExp.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ['gene']


class UpExpViewset(viewsets.ModelViewSet):
    serializer_class = UpExpSerializer
    queryset = UpExp.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ['gene']

class AnnotationViewset(viewsets.ModelViewSet):
    serializer_class = AnnotationSerializer
    queryset = Annotations.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ['gene']