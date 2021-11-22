from rest_framework import serializers
from .models import Food


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id' , 'author' ,'name' ,'body' , 'created_at' )
        model = Food