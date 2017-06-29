from django.contrib import admin
from profiles.models import *


class UserAdmin(admin.ModelAdmin):
	fields=['first_name','last_name','email','is_staff','is_active']
	list_display=('first_name','last_name','email','is_staff','is_active','date_joined')
	odering=('first_name','last_name','email')
	search_fields=('first_name','last_name','email')
	list_filter=['first_name','last_name','email']
 

admin.site.register(User,UserAdmin)
admin.site.register(Guichet)
