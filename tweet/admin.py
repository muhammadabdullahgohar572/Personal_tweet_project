from django.contrib import admin
from .models import Tweet
# Register your models here.


class showUserData(admin.ModelAdmin):
    list_display=('text','user')

admin.site.register(Tweet,showUserData)