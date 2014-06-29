#!/usr/bin/env python
from datetime import datetime, timedelta
import os.path
from sys import exit

from coinshot import Coinshot
from configobj import ConfigObj

class RudolphoError(Exception): pass

DEFAULT_APP_KEY = 'aqPNjNC1rb49cwAVy4M16CCcgtVEER'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'

config = ConfigObj(os.path.join(os.path.expanduser('~'), '.rudolpho'))

date_format = config.get('date_format')
if date_format is None or date_format == 'None' or date_format == '':
    date_format = DEFAULT_DATE_FORMAT

today = datetime.today().strftime(date_format)
yesterday = datetime.today() - timedelta(days=1)
yesterday = yesterday.strftime(date_format)

def _get_todos(td_filename, done=False):
    td_full_path = os.path.join(config.get('notes_path'), td_filename)
    if not os.path.exists(td_full_path):
        return None

    with open(td_full_path) as td_contents:
        if done:
            ret_list = [l for l in td_contents.readlines() if
                        l.startswith('[x]')]
        else:
            ret_list = [l.strip().replace('[ ]', '*') for l in \
                        td_contents.readlines() if l.startswith('[ ]')]

    return ret_list or None

todays_todos = _get_todos(today)
if todays_todos is None:
    exit(0)

yesterdays_todos = _get_todos(yesterday, done=True)

if yesterdays_todos is None:
    message = ''
else:
    num = len(yesterdays_todos)
    message = 'You completed %d tasks yesterday.\n' % num
    if num >= 5:
        message += 'Well done!\n'

message += '''
You have %d tasks to do today:
%s
''' % \
(len(todays_todos), '\n'.join(todays_todos))

coinshot_params = dict(message=message, title='To Do Today (%s)' % today,
                       priority=1)
app_key = config.get('pushover_app_key')
if app_key is None or app_key == 'None' or app_key == '':
    app_key = DEFAULT_APP_KEY

user_key = config.get('pushover_user_key', None)
if user_key is None or user_key == 'None' or user_key == '':
    key_path = config.get('pushover_key_path')
    if key_path is None:
        raise RudolphoError("either pushover_user_key or pushover_key_path " \
                            "must not be None!")
    user_key = open(key_path).read().strip()
    if user_key == '':
        raise RudolphoError("pushover_key_path file (%s) is empty!" % key_path)

coinshot = Coinshot(app_key=app_key, user_key=user_key)
coinshot.push(**coinshot_params)
