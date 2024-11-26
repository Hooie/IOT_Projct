#pir.py

import RPi.GPIO as GPIO
import time
import notification as noti
import socket
import threading

GPIO.setmode(GPIO.BCM)
pirPin = 8
GPIO.setup(pirPin, GPIO.IN)
global stop_threads

stop_threads = True


#while True:
 #   if GPIO.input(pirPin):
 #       t = time.localtime()
  #      print("%d:%d:%d 움직임 감지됨!!" %(t.tm_hour, t.tm_min, t.tm_sec))
   #     time.sleep(2)
    #else:
     #   print ("움직임 없음")
      #  time.sleep(0.05)


def start_socket_server():
    global stop_threads
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:

       server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	
       server.bind(('', 44443))
       server.listen(1)
       print('감시모드 제어 서버 on')
       print('---------------------------------')
       n = time.localtime()
       print("%d:%d:%d 시간부터 움직임 감지를 시작합니다." %(n.tm_hour, n.tm_min, n.tm_sec))	 
       client_socket, client_address = server.accept()
       with client_socket:
           print('연결됨!!')
           print('------------------------------')
           while stop_threads:
              data = client_socket.recv(1024).decode('utf-8')
              if int(data) == 0:
                 print('감시모드 종료!')
                 stop_threads = False
                 break

def detectmode():
    global stop_threads    
    print('감시모드 on!!')
    print('--------------------------------')
    
    while True:
       if GPIO.input(8):
          print('움직임 감지됨!')
          return True
          time.sleep(2)
       if stop_threads == False:
          break

def detecting_mode():
    global stop_threads    
    while stop_threads:
       if detectmode():
          noti.Notification()
          time.sleep(10)
	
def start_server():
    start_socket_server()

def start_mode():
      global stop_threads
      stop_threads = True
      try:
         motion_thread = threading.Thread(target=detecting_mode)
         server_thread = threading.Thread(target=start_server)
	
         motion_thread.start()
         server_thread.start()

         server_thread.join()	
         motion_thread.join()
	 
         print("감시모드 종료.. 원래 위치로 복귀")
		
      except KeyboardInterrupt:       
         print("프로그램 종료")
      finally:
         return
    
