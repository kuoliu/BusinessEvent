from django.contrib import admin

from models import *
# Register your models here.
class User_RandomAdmin(admin.ModelAdmin):
    list_display = ('user', 'random')

class User_MoreAdmin(admin.ModelAdmin):
    list_display = ('user', 'description', 'pic')

admin.site.register(User_Random, User_RandomAdmin)
admin.site.register(User_More, User_MoreAdmin)
