from django.conf.urls import url, include

from condottieri_notification.views import *

urlpatterns = [
    url(r'^list/$',
        NoticesListView.as_view(),
        name='condottieri_notification_list'
    ),
    url(r'^mark_all_seen/$',
        MarkAllSeenView.as_view(),
        name='condottieri_notification_mark_all_seen'
    ),
    url(r'', include('pinax.notifications.urls'))
]
