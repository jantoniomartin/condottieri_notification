from django.test import TestCase
from django.contrib.auth.models import User

from pinax.notifications import models as notifications

from condottieri_notification.models import *

class NoticeTest(TestCase):

    def setUp(self):
        self.user_0 = User.objects.create(
            username="user_0"
            )
        self.user_1 = User.objects.create(
            username="user_1"
            )
        self.notice = Notice.objects.create(
                recipient = self.user_0,
                sender = self.user_1,
                message = "message",
                notice_type = notifications.NoticeType.objects.first()
            )

    def test_unicode(self):
        self.assertEqual(str(self.notice), "message")

    def test_archive(self):
        self.assertIsNone(self.notice.archive())

    def test_is_unseen(self):
        self.assertEqual(self.notice.is_unseen(), True)
