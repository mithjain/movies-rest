from django.contrib.auth.models import User
from movies_api.models import Movies
from rest_framework import serializers

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = '__all__'