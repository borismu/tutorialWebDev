from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
	title = models.CharField()
	text = models.TextField()
	added_at = models.DateTimeField()
	rating = models.FloatField()
	author = models.ForeignKey(User)
	likes = models.ManyToManyField(User)

class Answer(models.Model):
	text = models.CharField()
	added_at = models.DateTimeField()
	author = models.ForeignKey(User)
	question = models.ForeignKey(Question)