import datetime

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

from pinax.notifications import models as notifications

class NoticeManager(models.Manager):
    def notices_for(self, user, archived=False, unseen=None, sent=False):
        if sent:
            lookup_kwargs = {"sender": user}
        else:
            lookup_kwargs = {"recipient": user}
        qs = self.filter(**lookup_kwargs)
        if not archived:
            qs = qs.filter(archived=archived)
        if unseen is not None:
            qs = qs.filter(unseen=unseen)
        return qs

    def unseen_count_for(self, recipient, **kwargs):
        return self.notices_for(recipient, unseen=True, **kwargs).count()

class Notice(models.Model):
    recipient = models.ForeignKey(User, related_name="received_notices",
        verbose_name=_("recipient"), on_delete=models.CASCADE)
    sender = models.ForeignKey(User, null=True, related_name="sent_notices",
        verbose_name=_("sender"), on_delete=models.CASCADE)
    message = models.TextField(_("message"))
    notice_type = models.ForeignKey(notifications.NoticeType,
        verbose_name=_("notice type"), on_delete=models.CASCADE)
    added = models.DateTimeField(_("added"), default=datetime.datetime.now)
    unseen = models.BooleanField(_("unseen"), default=True)
    archived = models.BooleanField(_("archived"), default=False)

    objects = NoticeManager()

    def __unicode__(self):
        return self.message

    def archive(self):
        self.archived = True
        self.save()

    def is_unseen(self):
        """
        Returns value of self.unseen, but also changes it to false.
        Use this in a template to mark an unseen notice differently the first
        time it is shown.
        """
        unseen = self.unseen
        if unseen:
            self.unseen = False
            self.save()
        return unseen

    class Meta:
        ordering = ["-added"]
        verbose_name = _("notice")
        verbose_name_plural = _("notices")
