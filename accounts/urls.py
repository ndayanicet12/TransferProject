from django.conf.urls import patterns, url
from . import views
app_name = 'accounts'
urlpatterns = patterns('',
    url(
        r'^login/$',
        'django.contrib.auth.views.login',
        name='login',
        kwargs={'template_name': 'accounts/login.html'}
    ),
    url(
        r'^logout/$',
        'django.contrib.auth.views.logout',
        name='logout',
        kwargs={'next_page': '/'}
    ),
)

"""
 
urlpatterns = patterns('',
     
    url(r'^connexion/$', views.connexion, name='connexion'),
    url(r'^deconnexion/$', views.deconnexion, name='deconnexion'),
 
    )
"""
