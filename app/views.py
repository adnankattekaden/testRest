from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializer import *

# Create your views here.

class Test(APIView):
    def get(self, request):
        data = Hai.objects.all()
        data_serializer = Haii(data, many=True)
        # return Response({"dskjb":"dskn"})
        print(data_serializer.data)
        return Response(data_serializer.data)


    def post(self, request):
        name = request.data['name']
        create = Hai.objects.create(name=name)
        data = Hai.objects.all()
        print(data)
        data_serializer = serializerHai(data, many=True)

        return Response(data_serializer.data)