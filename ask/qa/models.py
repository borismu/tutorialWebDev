from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
	title = models.CharField(max_length=50, blank=True)
	text = models.TextField(max_length=200, blank=True)
	added_at = models.DateTimeField(blank=True)
	rating = models.IntegerField(blank=True)
	author = models.ForeignKey(User, related_name="writtenqs", blank=True)
	likes = models.ManyToManyField(User, related_name="likedqs", blank=True)

class Answer(models.Model):
	text = models.TextField(max_length=200)
	added_at = models.DateTimeField()
	author = models.ForeignKey(User)
	question = models.ForeignKey(Question)