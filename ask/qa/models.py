from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class QuestionManager(models.Manager):
	def new(self):
		return self.order_by('-id')
	def popular(self):
		return self.order_by('-rating')

# Create your models here.
class Question(models.Model):
	objects = QuestionManager()

	title = models.CharField(max_length=50)
	text = models.TextField(max_length=200)
	added_at = models.DateTimeField(auto_now_add=True)
	rating = models.IntegerField(default=0)
	author = models.ForeignKey(User, related_name="writtenqs", blank=True, null=True)
	likes = models.ManyToManyField(User, related_name="likedqs", blank=True, null=True)

	def get_url(self):
		return reverse('question_detail',
			kwargs={'id':self.id})

	def __unicode__(self):
		return self.title


class Answer(models.Model):
	text = models.TextField(max_length=200)
	added_at = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(User, blank=True)
	question = models.ForeignKey(Question)