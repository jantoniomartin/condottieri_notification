from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.views.generic.base import View

from condottieri_notification.models import Notice

class NoticesListView(ListView):
    model = Notice
    context_object_name = 'notices'
    template_name = 'pinax/notifications/notices.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(NoticesListView, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        return Notice.objects.notices_for(self.request.user)

class MarkAllSeenView(View):
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(MarkAllSeenView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        Notice.objects.notices_for(request.user, unseen=True).update(unseen=False)
        return HttpResponseRedirect(reverse("condottieri_notification_list"))
