from django.utils.translation import ugettext

from pinax.notifications.backends.base import BaseBackend

class SiteBackend(BaseBackend):
    spam_sensitivity = 0
    
    def deliver(self, recipient, sender, notice_type, extra_context):
        context = self.default_context()
        context.update({
          "recipient": recipient,
          "sender": sender,
          "notice": ugettext(notice_type.display),  
        })
        context.update(extra_context)
        messages = self.get_formatted_messages(("notice.html",),
            notice_type.label, context)
        from condottieri_notification.models import Notice
        Notice.objects.create(
            recipient=recipient,
            sender=sender,
            message=messages["notice.html"],
            notice_type=notice_type
        )

