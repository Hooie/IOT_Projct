#py_program.py

import am2320sensor
import time
import smbus
import sys
import RPi.GPIO as GPIO
import io
import logging
import socket
import py_motor
import atexit
import subprocess
import pir

def send(sock):
	f = open('/home/user/hardware/TempHumid.txt', 'r')
	response = f.readlines()[-1]
	f.close()
	myresponse = response.encode('utf-8')
	sock.sendall(myresponse)
	print(response)

def handle_exit2():
	subprocess.run(["python", "/home/user/hardware/start_program.py"])

#소켓 정보 초기화
BUFSIZE = 1024
ADDR = ('', 44445)

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#포트 사용중일 때 발생하는 오류 해결
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
 
#포트 설정
serverSocket.bind(ADDR)
serverSocket.listen(1)
print("")
print("제어 서버 on")
print("----------------------")
print("서버 준비 갈 완료!!")
print("----------------------")

while True:
	print('연결 대기 중...')
	client_socket, client_address = serverSocket.accept()
	print('연결되었습니다!')
	data = client_socket.recv(1024).decode('utf-8')
	print('받은 데이터는: ', data)
	intdata = int(data)
	
	if not data:
		print("소켓 수신 오류!!")
		client_socket.close()
		continue
	
	#스위치 on
	if intdata == 1:
		print("1 받았습니다")
		py_motor.TurnOn()
		data = 0
		client_socket.close()
		# continue
	
	#스위치 off
	if intdata == 2:
		print("2 받았습니다")
		py_motor.TurnOff()
		data = 0
		client_socket.close()
		# continue
	
	#최근 온습도 전송하기
	if intdata == 3:
		send(client_socket)
		data = 0
		client_socket.close()
		# continue
	
	#감시모드 활성화 시
	if intdata == 4:
		client_socket.close()
		pir.start_mode()
		continue
	
	# print("다음 프로그램으로...")
	
	#except KeyboardInterrupt:
	# print('키보드 인터럽트 발생!! 종료합니다.')
	# GPIO.cleanup()
	
	#finally:
	# serverSocket.close()
	time.sleep(1)

exit()
