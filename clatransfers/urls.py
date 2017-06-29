from django.conf.urls import url

from . import views
 
app_name = 'clatransfers'
urlpatterns = [        
        ##########  Class based views   ###############


	url(r'^$', views.CreateTransfer.as_view(), name='createtransfer'),
	url(r'^createpaytransfer/$', views.CreatePayTransfer.as_view(), name='createpaytransfer'),
	url(r'^index/$', views.ListTransferEnvoye.as_view(), name='index'),
	url(r'^indexrecu/$', views.ListTransferRecu.as_view(), name='indexrecu'),
	url(r'^detailcreatetransfer/(?P<pk>\d+)/$',views.TransferDetail.as_view(), name='detailcreatetransfer'),
	url(r'^detailtransfer/(?P<pk>\d+)/$',views.TransferDetailRecu.as_view(), name='detailtransfer'),
	url(r'^createpaytransfer/(?P<pk>\d+)/$',views.CreatePayTransfer.as_view(), name='createpaytransfer'),

	url(r'^createtransfert/$', views.TransfertCreate.as_view(), name='createtransfert'),
	url(r'^delete/(?P<pk>\d+)/$',views.TransfertDelete.as_view(), name='delete'),
	url(r'^updatetransfert/(?P<pk>\d+)/$',views.TransfertUpdate.as_view(), name='updatetransfert'),
	url(r'^paytransfer/$',views.paytransfer, name='paytransfer'),


	#url(r'^print_transfers/$',views.print_transfers, name='print_transfers'),

	#url(r'^(?P<pk>[0-9]+)/results/$',views.ResultsView.as_view(), name='results'),
	#url(r'^(?P<question_id>[0-9]+)/vote/$',views.vote, name='vote'),
]

