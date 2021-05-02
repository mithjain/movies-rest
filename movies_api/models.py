from django.db import models

# Create your models here.
class Movies(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=120)
    director = models.CharField(max_length=120)
    genre = models.CharField(max_length=120)
    rating = models.IntegerField()
    release_data = models.DateField()
    
    class Meta:
        ordering = ['-id']
        