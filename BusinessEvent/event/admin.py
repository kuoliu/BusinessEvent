from django.contrib import admin

from models import *
# Register your models here.
class User_RandomAdmin(admin.ModelAdmin):
    list_display = ('user', 'random')

class User_MoreAdmin(admin.ModelAdmin):
    list_display = ('user', 'description', 'pic')

class Event_Admin(admin.ModelAdmin):
    list_display = ('name', 'description', 'pic')

class News_Admin(admin.ModelAdmin):
    list_display = ('event', 'media', 'tag', 'abstract', 'content', 'pic', 'check')

admin.site.register(User_Random, User_RandomAdmin)
admin.site.register(User_More, User_MoreAdmin)
admin.site.register(Event, Event_Admin)
admin.site.register(News, News_Admin)
