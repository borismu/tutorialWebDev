from django import forms
from qa.models import Answer, Question

class AskForm(forms.Form):
	title = forms.CharField(max_length = 50)
	text = forms.CharField(max_length = 200, widget = forms.Textarea)

	def save(self):
		self.cleaned_data['author_id'] = self._user
		return Question.objects.create(**self.cleaned_data)

class AnswerForm(forms.Form):
	text = forms.CharField(max_length = 200, widget = forms.Textarea)
	question = forms.IntegerField()

	def save(self):
		self.cleaned_data['author'] = self._user
		return Question.objects.create(**self.cleaned_data)