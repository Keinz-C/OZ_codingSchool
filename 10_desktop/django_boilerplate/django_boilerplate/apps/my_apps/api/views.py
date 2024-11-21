from django.shortcuts import render
from rest_framework import mixins, generics
from .models import MyModel
from .serializers import MyModelSerializer

class MyModelView(generics.GenericAPIView):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer
