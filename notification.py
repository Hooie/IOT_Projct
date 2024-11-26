#notification.py

import firebase_admin
from firebase_admin import credentials
from firebase_admin import messaging
import time

cred = credentials.Certificate("/home/user/hardware/cert_key.json")
default_app = firebase_admin.initialize_app(cred)

registration_token = 'c7I9RS__R1OtvgkEA6DM14:APA91bG7ypZc9SAazrmKOapWa0gZd0Wx5VgUEfgTMOX_oNXRqDrQI2i1mn_5SMutXCWwhEKWNPrasKkgcV_s44-ArgYlPJZ-1snJOckQVokOrFM47iUArBM' #내 폰
#registration_token = 'fTocxigTQVin6pNupUFScW:APA91bE0F3EyzWMvh6t1pwxMK2Lnl246L4ZSPMdEfaPGoMSGAoVaUIQFGnXX3ppuVtXASmgIziHNS2npazU8P4xj4B8j1vgKLQDDAhFjHaelvGYgyKQWLEQ' # 수호 안드


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
		
