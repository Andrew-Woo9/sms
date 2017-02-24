from django.shortcuts import render

from sms.forms import SMSForm
import json
import os
import sys

from sdk.api.message import Message
from sdk.exceptions import CoolsmsException

from sms.settings import config


def index(request):

    if request.method == 'POST':
        form = SMSForm(request.POST)
        if form.is_valid():

            numbers = form.cleaned_data['recipient_numbers']

            api_key = config['sms']['api_key']
            api_secret = config['sms']['api_secret']

            # SMS_TO = request.get('recipient_numbers')
            # SMS_from = '01029953874'
            # SMS_text = request.get('content')

            params = {
                'type': 'sms',
                'to': '01066273389',
                'from': '01029953874',
                'text': 'SMS 인가?',
            }

            cool = Message(api_key, api_secret)

            try:
                response = cool.send(params)
                print("Success Count : %s" % response['success_count'])
                print("Error Count : %s" % response['error_count'])
                print("Group ID : %s" % response['group_id'])

                if "error_list" in response:
                    print("Error List : %s" % response['error_list'])

            except CoolsmsException as e:
                print("Error Code : %s" % e.code)
                print("Error Message : %s" % e.msg)

            sys.exit()

    else:
        form = SMSForm()



    context = {
        'form': form,
    }
    return render(request, 'sms/index.html', context)