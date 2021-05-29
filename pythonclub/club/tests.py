from django.test import TestCase
from django.contrib.auth.models import User
from .models import Meeting, MeetingMinutes, Resource, Event
import datetime

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
       self.resource=Resource(resourcename='Zoom Meetings', resourcetype='For Virtual Meetings', URL='https://zoom.us/', dateentered=('5/28/21'), user=self.user, description='N/A')

   def test_string(self):
       self.assertEqual(str(self.resource), 'Zoom Meetings')

   def test_tablename(self):
       self.assertEqual(str(Resource._meta.db_table), 'resource')
