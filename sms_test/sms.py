import json
import os

CUR_PATH = os.path.abspath(__file__)
SMS_TEST_PATH = os.path.dirname(CUR_PATH)
ROOT_PATH = os.path.dirname(SMS_TEST_PATH)
CONF_PATH = os.path.join(ROOT_PATH, '.conf')

config = json.loads(open(os.path.join(CONF_PATH, 'settings_local.json')).read())
