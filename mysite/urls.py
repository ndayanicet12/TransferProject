
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^login/', auth_views.login, {'template_name':'accounts/login.html'}, name='login'),  
    url(r'^logout/', auth_views.logout,{'next_page':'/login/'},name='logout'),
    url(r'^polls/', include('polls.urls')),
    url(r'^transfers/', include('transfers.urls')),
    url(r'^clatransfers/', include('clatransfers.urls')),

    url(r'^admin/', admin.site.urls),    
]

