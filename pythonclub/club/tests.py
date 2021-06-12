from django.test import TestCase
from django.contrib.auth.models import User
from .models import Meeting, MeetingMinutes, Resource, Event
import datetime
from .forms import ResourceForm, MeetingForm
from django.urls import reverse_lazy, reverse

# Create your tests here.

class MeetingTest(TestCase):
   def setUp(self):
       self.type=Meeting(meetingtitle='Meeting 1', meetingdate=('5/29/21'), meetingtime='1:30 PM', location='Virtual', agenda='Setup')

   def test_typestring(self):
       self.assertEqual(str(self.type), 'Meeting 1')

   def test_tablename(self):
       self.assertEqual(str(Meeting._meta.db_table), 'meeting')

class ResourceTest(TestCase):
   def setUp(self):
       self.type=Resource(resourcename='Zoom Meetings')
       self.user=User(username='user1')
       self.resource=Resource(resourcename='Zoom Meetings', resourcetype='For Virtual Meetings', URL='https://zoom.us/', dateentered=5/28/21, user=self.user, description='N/A')

   def test_string(self):
       self.assertEqual(str(self.resource), 'Zoom Meetings')

   def test_tablename(self):
       self.assertEqual(str(Resource._meta.db_table), 'resource')


class NewResourceTest(TestCase):
    def test_resourceform(self):
        data={
            'resourcename':'Full Stack Python - Django', 
            'resourcetype':'Resource', 
            'URL':'https://www.fullstackpython.com/django.html', 
            'dateentered':'6/2/21', 
            'user':'hanan', 
            'description':'N/A'
        }
        form=ResourceForm (data)
        self.assertTrue(form.is_valid)

class NewMeetingTest(TestCase):
    def test_meetingform(self):
        data={
            'meetingtitle':'Meeting 4', 
            'meetingdate':'6/4/21', 
            'meetingtime':'1:30 PM', 
            'location':'Virtual', 
            'agenda':'Setup continued'
        }
        form=MeetingForm (data)
        self.assertTrue(form.is_valid)

class New_Meeting_Authentication_Test(TestCase):
    def setUp(self):
        self.test_user=User.objects.create_user(username='testuser1', password='P@ssw0rd1')
        self.type=Meeting.objects.create(meetingtitle='Meeting 4')
        self.meeting=Meeting.objects.create(meetingtitle='Meeting 4', meetingdate='2021-06-11', meetingtime='1:30 PM', location='Virtual', agenda='Setup')

    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newmeeting'))
        self.assertRedirects(response, '/accounts/login/?next=/club/newmeeting/')