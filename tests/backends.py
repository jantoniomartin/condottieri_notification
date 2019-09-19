from django.test import TestCase
from django.template.exceptions import TemplateDoesNotExist

from pinax.notifications import models as notifications

from condottieri_notification.backends import SiteBackend

class SiteBackendTestCase(TestCase):

    def _test_deliver(self):
        class DummyObject:
            pass
        recipient = DummyObject()
        sender = DummyObject()
        notice_type = notifications.NoticeType.objects.first()
        extra_context = {}
        backend = SiteBackend(medium_id=1)
        self.assertRaises(backend.deliver(recipient, sender, notice_type, extra_context),
                TemplateDoesNotExist)
