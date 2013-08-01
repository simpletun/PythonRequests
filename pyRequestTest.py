'''
Created on Aug 1, 2013

@author: olsena
'''

import sys
import datetime
import time
import requests

url = 'https://adx.webtrends.com/v3/Reporting/profiles/60856/Keymetrics/?start_period=2013m04d12&end_period=2013m05d16&language=en-US&format=html&suppress_error_codes=true'


r = requests.get(url, auth=('motorcycleusa\olsena', 'intern@l'), verify=False)

f = open('testout.html', 'w')
f.write(r.text)
f.close()


