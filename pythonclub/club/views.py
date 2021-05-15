from django.shortcuts import render
from .models import Meeting, MeetingMinutes, Resource, Event

# Create your views here.
def index(request):
    return render(request, 'club/index.html')

def meeting(request):
    meeting_list=Meeting.objects.all()
    return render(request, 'club/meeting.html', {'meeting_list' : meeting_list})