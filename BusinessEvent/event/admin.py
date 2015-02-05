from django.contrib import admin

from models import *
# Register your models here.
class User_RandomAdmin(admin.ModelAdmin):
    list_display = ('user', 'random')

class User_MoreAdmin(admin.ModelAdmin):
    list_display = ('user', 'description', 'pic', 'role')

class Event_Admin(admin.ModelAdmin):
    list_display = ('name', 'tag', 'description', 'pic')

class News_Admin(admin.ModelAdmin):
    list_display = ('datetime', 'event', 'media', 'tag', 'abstract', 'content', 'pic', 'check')

class UserMore_Event_Admin(admin.ModelAdmin):
    list_display = ('user_more', 'event')

class UserMore_News_Admin(admin.ModelAdmin):
    list_display = ('user_more', 'news')

admin.site.register(User_Random, User_RandomAdmin)
admin.site.register(User_More, User_MoreAdmin)
admin.site.register(Event, Event_Admin)
admin.site.register(News, News_Admin)
admin.site.register(UserMore_Event, UserMore_Event_Admin)
admin.site.register(UserMore_News, UserMore_News_Admin)

