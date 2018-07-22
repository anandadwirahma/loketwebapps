from django.conf.urls import include, url
from django.contrib import admin

import event.views as event

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^event/', event.view_event, name='event'),
    url(r'^createEvent/', event.create_event, name='createEvent'),
    url(r'^submitEvent/', event.submit_event, name='submitEvent'),
    url(r'^ticket/', event.view_createticket, name='ticket'),
    url(r'^submitTicket/', event.submit_ticket, name='submitTicket'),
    url(r'^transaction/', event.view_createtrx, name='transaction'),
    url(r'^submitTrx/', event.submit_trx, name='submitTrx'),
]