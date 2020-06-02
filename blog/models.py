from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from star_ratings.models import Rating

# Create your models here.
class Post(models.Model):
    music_url = models.URLField(default='') 
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    ratings = GenericRelation(Rating, related_query_name='posts')

    def __str__(self):
        return self.title


