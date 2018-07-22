# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import redirect

import requests
import random
import string
import json

class WebView(TemplateView):
    template_name = ''

urlapi = 'http://127.0.0.1:8000/'

def view_event(request):
    resp = requests.get(urlapi + "api/event/getinfo/")

    data = []
    for row in resp.json():
        data.append(
            {
                'eventname': row['eventname'],
                'evenstart': row['evenstart'],
                'evenend': row['evenend'],
                'id': row['id']
            }
        )

    return render(request, 'event/v_event.html', {'data' : data})

def create_event(request):
    return render(request, 'event/v_createEvent.html')

def submit_event(request):
    dataform = request.POST
    eventname = dataform.get('eventname')
    eventtime = dataform.get('eventtime')
    locname = dataform.get('locname')
    locmap = dataform.get('locmap')
    address = dataform.get('address')
    city = dataform.get('city')
    eventid = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
    locid = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))

    splittime = eventtime.split("-",1)
    eventstart = splittime[0]
    eventend = splittime[1]

    payloadevent = {
        'eventname': eventname,
        'evenstart': eventstart.replace(" ", ""),
        'evenend': eventend.replace(" ", ""),
        'id': eventid
    }
    headers = {'content-type': 'application/json'}
    requests.post(urlapi + "api/event/create/", data=json.dumps(payloadevent), headers=headers)

    payloadlocation = {
        'city': city,
        'event_id': eventid,
        'locname': locname,
        'locmap': locmap,
        'address' : address,
        'id' : locid
    }
    headers = {'content-type': 'application/json'}
    requests.post(urlapi + "api/location/create/", data=json.dumps(payloadlocation), headers=headers)

    return redirect('/event/')

def view_createticket(request):
    return render(request, 'ticket/v_createTicket.html')

def submit_ticket(request):
    dataform = request.POST
    eventid = dataform.get('eventid')
    type = dataform.get('type')
    price = dataform.get('price')
    qty = dataform.get('qty')
    ticketid = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))

    payloadticket = {
        'event_id': eventid,
        'price': price,
        'type': type,
        'id': ticketid,
        'qty': qty
    }
    headers = {'content-type': 'application/json'}
    requests.post(urlapi + "api/event/ticket/create", data=json.dumps(payloadticket), headers=headers)

    return redirect('/event/')

def view_createtrx(request):
    return render(request, 'trx/v_createTrx.html')

def submit_trx(request):
    dataform = request.POST
    eventid = dataform.get('eventid')
    custname = dataform.get('custname')
    trxid = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))

    payloadtrx = {
        'custname': custname,
        'datetrx': "",
        'event_id': eventid,
        'id': trxid
    }
    headers = {'content-type': 'application/json'}
    requests.post(urlapi + "api/transaction/purchase/", data=json.dumps(payloadtrx), headers=headers)

    return redirect('/event/')