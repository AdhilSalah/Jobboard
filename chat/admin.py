from django.contrib import admin

from chat.models import Messages, Room

# Register your models here.
admin.site.register(Room)
admin.site.register(Messages)