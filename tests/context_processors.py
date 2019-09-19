from django.test import TestCase
from django.test.client import RequestFactory
from django.contrib.auth.models import User, AnonymousUser

from condottieri_notification.context_processors import notification

class ContextProcessorsTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user_0 = User.objects.create(
            username="user_0"
            )
    
    def test_notification_authenticated(self):
        request = self.factory.get('/')
        request.user = self.user_0
        r = notification(request)
        self.assertEqual(r["notice_unseen_count"], 0)
    
    def test_notification_anonymous(self):
        request = self.factory.get('/')
        request.user = AnonymousUser()
        r = notification(request)
        self.assertEqual(r, {})
