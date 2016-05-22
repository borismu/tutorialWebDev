from django.contrib import admin

# Register your models here.
from qa.models import Question, Answer

class QuestionAdmin(admin.ModelAdmin):
	list_display = ('title', 'text', 'rating', 'author')

admin.site.register(Question, QuestionAdmin)