#startprogram.py

import os
import socket
import atexit
import subprocess

def send(sock):
	f = open('/home/teaho/sensor/TempHumid.txt', 'r')
	response = f.readlines()[-1]
	f.close()
	myresponse = response.encode('utf-8')
	sock.sendall(myresponse)
	print(response)

def handle_exit():
	subprocess.run(["python", "/home/teaho/sensor/py_program.py"])

atexit.register(handle_exit)

#소켓 정보 초기화
BUFSIZE = 1024
ADDR = ('', 44444)

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#포트 사용중일 때 발생하는 오류 해결
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#포트 설정
serverSocket.bind(ADDR)
serverSocket.listen(1)
print("로그인 온습도 서버 ON")
print("----------------------")
print("서버 준비 갈 완료!!")
print("----------------------")
print('연결 대기 중...')
client_socket, client_address = serverSocket.accept()
print('연결되었습니다!')

data = client_socket.recv(1024)
data = data.decode('utf-8')
print('받은 데이터는: ', data)
intdata = int(data)

if intdata == 3:
	send(client_socket)
	data = 0
	client_socket.close()
	
exit()
