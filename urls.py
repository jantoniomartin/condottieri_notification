from django.conf.urls import *

from condottieri_notification.views import *

urlpatterns = patterns('condottieri_notification.views',
    url(r'^list/$',
        NoticesListView.as_view(),
        name='condottieri_notification_list'
    ),
    url(r'^mark_all_seen/$',
        MarkAllSeenView.as_view(),
        name='condottieri_notification_mark_all_seen'
    ),
    url(r'', include('pinax.notifications.urls'))
)
