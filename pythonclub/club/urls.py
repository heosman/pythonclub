from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('resource/', views.resource, name='resource'),
    path('meeting/', views.meeting, name='meeting'),
    path('meetingdetail/<int:id>', views.meetingdetail, name='detail'),
    path('newresource/', views.newResource, name='newresource'),
    path('newmeeting/', views.newMeeting, name='newmeeting'),
]