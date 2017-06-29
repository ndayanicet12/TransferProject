from django.conf.urls import url

from polls import views
 
app_name = 'polls'
urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^addQuestion/$', views.addQuestion, name='addQuestion'),
	url(r'^newquestion/$', views.CreateQuestionView.as_view(), name='newquestion'),
        url(r'^editquestion/(?P<pk>\d+)/$',views.UpdateQuestionView.as_view(),name='editquestion'),
        url(r'^deletequestion/(?P<pk>\d+)/$',views.DeleteQuestionView.as_view(),name='deletequestion'),
        url(r'^listequestions/$', views.ListQuestionView.as_view(), name='listequestions'),

        url(r'^deletechoice/(?P<pk>\d+)/$',views.DeleteChoiceView.as_view(),name='deletechoice'),
        url(r'^editchoice/(?P<pk>\d+)/$',views.UpdateChoiceView.as_view(),name='editchoice'), 
	url(r'^newchoice/$', views.CreateChoiceView.as_view(), name='newchoice'),       
	url(r'^addChoice/$', views.addChoice, name='addChoice'),
	url(r'^listechoices/$', views.ListChoiceView.as_view(), name='listechoices'),
	url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(), name='detail'),
	url(r'^(?P<pk>[0-9]+)/results/$',views.ResultsView.as_view(), name='results'),
	url(r'^(?P<question_id>[0-9]+)/vote/$',views.vote, name='vote'),




#""""
#url(r'^new$', views.question_create, name='new'),
#url(r'^edit/(?P<pk>\d+)$', views.question_update, name='edit'),
#url(r'^delete/(?P<pk>\d+)$', views.question_delete, name='delete'),
#""""

]



