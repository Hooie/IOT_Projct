#temp_program.py

import time
import am2320sensor

am2320sensor.WakeSensor()


while True:
    try:
        while True:
            t = am2320sensor.ReadTemperature()
            h = am2320sensor.ReadHumidity()
            tl = time.localtime()
            f = open('/home/user/hardware/TempHumid.txt', 'a')
            date = (time.strftime("%Y-%m-%d", time.localtime(time.time())))
            #print("%d:%d:%d" %(tl.tm_hour,tl.tm_min,tl.tm_sec), end='')
            #print(" 온도: ", t, "℃", end='')
            #print(" 습도: ", h, "%")
            strsave = str(date) + '-' + str(tl.tm_hour) + ':' + str(tl.tm_min) + ':' + str(tl.tm_sec) + '  ' + str(t) + '℃'+ ' ' + str(h) + '%'
            f.write(strsave+'\n')
            print(strsave+'\n')
            f.close()
            time.sleep(600)

    except KeyboardInterrupt:
        f.close()
