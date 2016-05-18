from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
	title = models.CharField(max_length=50)
	text = models.TextField(max_length=200)
	added_at = models.DateTimeField()
	rating = models.FloatField()
	author = models.ForeignKey(User, related_name="writtenqs")
	likes = models.ManyToManyField(User, related_name="likedqs")

class Answer(models.Model):
	text = models.TextField(max_length=200)
	added_at = models.DateTimeField()
	author = models.ForeignKey(User)
	question = models.ForeignKey(Question)