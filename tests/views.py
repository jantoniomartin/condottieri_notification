from django.urls import reverse
from django.test import TestCase
from django.test.client import RequestFactory
from django.contrib.auth.models import User

from condottieri_notification.views import *

class NoticesListViewTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user_0 = User.objects.create(
            username="user_0"
            )
        self.user_1 = User.objects.create(
            username="user_1"
            )

    def test_notification_list(self):
        request = self.factory.get(
            reverse('condottieri_notification_list')
        )
        request.user = self.user_0
        response = NoticesListView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_mark_all_seen(self):
        request = self.factory.get(
            reverse('condottieri_notification_mark_all_seen')
        )
        request.user = self.user_0
        response = MarkAllSeenView.as_view()(request)
        self.assertEqual(response.status_code, 302)

