
"""
from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect, HttpResponse
#from django.http import 
from django.core.urlresolvers import reverse
from django.template import loader
from .models import Question, Choice

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

"""

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import timezone

from django.core.urlresolvers import reverse
from django.views import generic
from .models import Choice, Question
from polls.forms import *
from django.views.generic import *


# Create,Update and Delete with CBV ###
 
class CreateQuestionView(CreateView):
      model = Question
      fields = '__all__'
      template_name = 'polls/newquestion.html'

      def get_success_url(self):
          return reverse('polls:listequestions')

      def get_context_data(self,**kwargs):
           context = super(CreateQuestionView, self).get_context_data(**kwargs)
           context['action'] = reverse('polls:newquestion')
           return context


class UpdateQuestionView(UpdateView):
     model = Question
     fields = '__all__'
     template_name = 'polls/editquestion.html'

     def get_success_url(self):
         return reverse('polls:listequestions')


     def get_context_data(self,**kwargs):
           context = super(UpdateQuestionView, self).get_context_data(**kwargs)
           context['action'] = reverse('polls:editquestion', kwargs={'pk': self.get_object().id})
           return context 


class DeleteQuestionView(DeleteView):
      model = Question
      template_name = 'polls/deletequestion.html'
      def get_success_url(self):
          return reverse('polls:listequestions')



class CreateChoiceView(CreateView):
      model = Choice
      fields = '__all__'
      template_name = 'polls/newchoice.html'

      def get_success_url(self):
          return reverse('polls:listechoices')


      def get_context_data(self,**kwargs):
           context = super(CreateChoiceView, self).get_context_data(**kwargs)
           context['action'] = reverse('polls:newchoice')
           return context


class UpdateChoiceView(UpdateView):
     model = Choice
     fields = '__all__'
     template_name = 'polls/editchoice.html'

     def get_success_url(self):
         return reverse('polls:listechoices')


     def get_context_data(self,**kwargs):
           context = super(UpdateChoiceView, self).get_context_data(**kwargs)
           context['action'] = reverse('polls:editchoice', kwargs={'pk': self.get_object().id})
           return context 


class DeleteChoiceView(DeleteView):
      model = Choice
      template_name = 'polls/deletechoice.html'
      def get_success_url(self):
          return reverse('polls:listechoices')



## Update Delete with FVB  ###

def question_create(request, template_name='polls/question_form.html'):
    form = FormQuestion(request.POST)
    if form.is_valid():
        form.save()
        return redirect('polls/listequestions.html')
    return render(request, template_name, {'form':form})

def question_update(request, idq, template_name='polls/question_form.html'):
    question = get_object_or_404(question, pk=idq)
    form = FormQuestion(request.POST or None, instance=question)
    if form.is_valid():
        form.save()
        return redirect('polls:listequestions')
    return render(request, template_name, {'form':form})

def question_delete(request, idq, template_name='polls/question_delete.html'):
    question = get_object_or_404(question, pk=idq)    
    if request.method=='POST':
        question.delete()
        return redirect('polls:listequestions')
    return render(request, template_name, {'object':question})


def  addQuestion(request):
	save=False
	if request.method=='POST':
		form=FormQuestion(request.POST)
		if form.is_valid():		
		   #q =Question.objects.create(question_text=request.POST['question_text'], pub_date=timezone.now())
		   question_text=form.cleaned_data['question_text']
		   pub_date=form.cleaned_data['pub_date']
                   form.save()
		   #print q.question_text
		   #save=True
		   return render(request, 'polls/listequestions.html')
                  
	else:
              	form=FormQuestion()
        return render(request,
                    'polls/addQuestion.html',
                    {'form':form}
                )


def  addChoice(request):
	save=False
	if request.method=='POST':
		form=FormChoice(request.POST)
		if form.is_valid():		
		   #q =Question.objects.create(question_text=request.POST['question_text'], pub_date=timezone.now())
		   question=form.cleaned_data['question']
		   choice_text=form.cleaned_data['choice_text']
		   votes=form.cleaned_data['votes']
		   
		   form.save()
		   #print q.question_text
		   #save=True
		   return render(request, 'polls/listechoices.html')
                  
	else:
              	form=FormChoice()
        return render(request,
                    'polls/addChoice.html',
                    {'form':form}
                )



class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'


    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:50]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
 
class ListQuestionView(generic.ListView):
	model = Question
	template_name='polls/listequestions.html'
	#context_object_name='question_list'

	def get_queryset(self):
		return Question.objects.all()

class ListChoiceView(generic.ListView):
	model = Choice
	template_name='polls/listechoices.html'
	#context_object_name='choice_list'

	def get_queryset(self):
		return Choice.objects.all()

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
