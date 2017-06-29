from django.contrib import admin

# Register your models here.
from polls.models import Question,Choice

class QuestionAdmin(admin.ModelAdmin):
	fields=['pub_date','question_text']
	list_display=('question_text','pub_date')
	odering=('question_text')
	search_fields=('question_text',)
	list_filter=['pub_date']
"""
	fieldsets=[
		('Question Information',{'fields':['question_text']}),
		('Date Information',{'fields':['pub_date']}),
	]
"""

admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)
