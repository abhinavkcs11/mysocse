from django.shortcuts import render,redirect
from django.contrib.auth import logout
from eventsapp.models import *
from announcementsapp.models import *
# Create your views here.
def indexview(request):
    # print(request.user.get_full_name())
    events = EventModel.objects.all()
    announcements = AnnouncementsModel.objects.all()
    if request.user.is_authenticated:
        context = {
            'user' : request.user,
            'events' : events,
            'announcements' :announcements
            }
        return render(request,"socseapp/homepage.html",context)
    context = {
        'events' : events,
        'announcements' : announcements
        }
    return render(request,"socseapp/index.html",context)

def logoutuser(request):
    logout(request)
    return redirect("account_logout")