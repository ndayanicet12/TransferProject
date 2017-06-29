from django import forms
from polls.models import *

class QuestionForm(forms.Form):
        pub_date=forms.DateTimeField()
	question_text=forms.CharField(max_length=1000)

class FormQuestion(forms.ModelForm):			
	class Meta:
		model=Question
		fields='__all__'


class FormChoice(forms.ModelForm):			
	class Meta:
		model=Choice
		fields='__all__'



