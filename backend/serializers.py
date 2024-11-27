from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Destination, Continent

class ContinentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Continent
        fields = ['id', 'name']

class DestinationSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(source='user', queryset=User.objects.all())
    continent = serializers.PrimaryKeyRelatedField(queryset=Continent.objects.all(), required=False, allow_null=True)
    isLiked = serializers.BooleanField(source='is_liked', required=False)
    details = serializers.CharField(source='description', required=False)
    visitedDate = serializers.DateField(source='visited_date', required=False)

    class Meta:
        model = Destination
        fields = [
            'id',
            'name',
            'country',
            'continent',
            'details',
            'isLiked',
            'visitedDate',
            'user_id',
        ]
        extra_kwargs = {
            'isLiked': {'required': False},
            'details': {'required': False},
            'visitedDate': {'required': False},
        }

    def create(self, validated_data):
        visited_date = validated_data.pop('visited_date', None)
        destination = Destination.objects.create(**validated_data)
        if visited_date:
            destination.visited_date = visited_date
            destination.save()
        return destination