# coding=utf-8
import requests
import datetime as dt
import urllib.parse
from googleapiclient.discovery import build


api_key = ''
calendar_id = 'japanese__ja@holiday.calendar.google.com'

# APIを叩く

service = build(serviceName='calendar', version='v3', developerKey=api_key)
events = service.events().list(calendarId=calendar_id).execute()



# 見づらいのでソート
for item in sorted(events['items'], key=lambda item: item['start']['date']):
    print(item)
#    print(u'{0}\t{1}'.format(item['start']['date'], item['summary']))


