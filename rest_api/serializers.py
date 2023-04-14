from rest_framework import serializers
from api.models import *

# create your serializers here

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'