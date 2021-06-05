from django.shortcuts import render,redirect
from .models import EventModel
from django.contrib.auth.models import User
# Create your views here.
def register_into_event(request,userid,eventid):
    user = User.objects.get(id = userid)
    event = EventModel.objects.get(id = eventid)
    event.participants.add(user)
    return redirect(request.META['HTTP_REFERER'])

def unregister_from_event(request,userid,eventid):
    user = User.objects.get(id = userid)
    event = EventModel.objects.get(id = eventid)
    event.participants.remove(user)
    return redirect(request.META['HTTP_REFERER'])
