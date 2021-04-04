from rest_framework import serializers
from .models import *

class Haii(serializers.Serializer):
    class Meta:
        model = Hai
        feilds = ('name',)