import json
import os
import sys

from sdk.api.message import Message
from sdk.exceptions import CoolsmsException

CUR_PATH = os.path.abspath(__file__)
SMS_TEST_PATH = os.path.dirname(CUR_PATH)
ROOT_PATH = os.path.dirname(SMS_TEST_PATH)
CONF_PATH = os.path.join(ROOT_PATH, '.conf')

config = json.loads(open(os.path.join(CONF_PATH, 'settings_local.json')).read())

api_key = config['sms']['api_key']
api_secret = config['sms']['api_secret']

SMS_TO = '01066273389'
SMS_from = '01029953874'
SMS_text = 'SMS TEST'


params = {
    'type': 'sms',
    'to': SMS_TO,
    'from': SMS_from,
    'text': SMS_text,
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

