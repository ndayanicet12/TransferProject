from django.conf.urls import url

from . import views
 
app_name = 'transfers'
urlpatterns = [
        ##########  Functions based views   ###############

	url(r'^$', views.addtransfer, name='addtransfer'),
	url(r'^index/$', views.index, name='index'),
	url(r'^validtransfer/$',views.validtransfer, name='validtransfer'),
	url(r'^paytransfer/$',views.paytransfer, name='paytransfer'),
	url(r'^updatetransfer/(?P<pk>\d+)/$',views.updatetransfer, name='updatetransfer'),
	url(r'^transferdetail/(?P<pk>\d+)/$',views.transferdetail, name='transferdetail'),
	url(r'^transferdetailrecu/(?P<pk>\d+)/$',views.transferdetailrecu, name='transferdetailrecu'),
        url(r'^listeTransfersPayes/$', views.listeTransfersPayes, name='listeTransfersPayes'),
 
        
        ##########  Class based views   ###############


	url(r'^createtransfer/$', views.CreateTransfer.as_view(), name='createtransfer'),
	url(r'^createpaytransfer/$', views.CreatePayTransfer.as_view(), name='createpaytransfer'),

	#url(r'^(?P<pk>[0-9]+)/results/$',views.ResultsView.as_view(), name='results'),
	#url(r'^(?P<question_id>[0-9]+)/vote/$',views.vote, name='vote'),
]

