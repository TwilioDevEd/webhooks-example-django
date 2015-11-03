from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^voice', 'webhooks.views.incoming_call', name='incoming_call'),
    url(r'^message', 'webhooks.views.incoming_message', name='incoming_message'),

    # Django admin
    url(r'^admin/', include(admin.site.urls)),
]
