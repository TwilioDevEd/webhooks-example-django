from django.conf.urls import include, url
from django.contrib import admin

from webhooks import views as webhook_views

urlpatterns = [
    url(r'^voice', webhook_views.incoming_call, name='incoming_call'),
    url(r'^message', webhook_views.incoming_message, name='incoming_message'),

    # Django admin
    url(r'^admin/', include(admin.site.urls)),
]
