#notification.py

import firebase_admin
from firebase_admin import credentials
from firebase_admin import messaging
import time

cred = credentials.Certificate("/home/teaho/sensor/cert_key.json")
default_app = firebase_admin.initialize_app(cred)

registration_token = 'd-7TiM_kTDKz_NUVApuZI6:APA91bEpTsLU0v6uO0jFUKz8vA4_yHrp4srbvJs_bZKB_NBlq_CbfmnDNMmlAa73sdU5SCgWXbrE5jRxG9MfUti-xjLm8c14r8NCFHIeF86yNDbwy4g6DLg'

def Notification():
	message = messaging.Message(
	notification=messaging.Notification(
				title='Smart Home Care System',
				body='움직임이 감지되었습니다!! CCTV를 확인해주세요!!'
				),
				data = {
					'title':'smart home care system',
					'message':'움직임이 감지되었습니다!! CCTV를 확인해주세요',
					'mode':'test',
					'data':'12345'
				},
				token=registration_token,
	)
	
	response = messaging.send(message)
	print('알림 전송 완료!!', response)
