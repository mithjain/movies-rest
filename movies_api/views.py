from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from movies_api.serializers import MovieSerializer
from .models import Movies
# Create your views here.
class ListCreateMovieAPIView(ListCreateAPIView):
    serializer_class = MovieSerializer
    queryset = Movies.objects.all()

    def perform_create(self, serializer):
        serializer.save()
