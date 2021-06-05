from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(EventModel)
class EventModelAdmin(admin.ModelAdmin):
    list_display = ("event_name","description")
    def get_ordering(self, request):
        return ['id']
