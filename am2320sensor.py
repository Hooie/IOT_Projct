#am2320sensor.py
import smbus
import time

i2cbus = 1
addr = 0x5c
bus = smbus.SMBus(i2cbus)

def WakeSensor():
    while True:
        try:
            bus.write_i2c_block_data(addr, 0x00, [])
            break
        except IOError:
            pass
    time.sleep(0.003)

def ReadTemperature():
    global block
    WakeSensor()
    while True:
        try:
            bus.write_i2c_block_data(addr, 0x03, [0x02, 0x02])
            break
        except IOError:
            pass
       
    time.sleep(0.015)
   
    try:
        block = bus.read_i2c_block_data(addr, 0, 4)
    except IOError:
        pass
   
    temperature = float(block[2] << 8 | block[3]) / 10
    return temperature

def ReadHumidity():
    global block
    WakeSensor()
    while True:
        try:
            bus.write_i2c_block_data(addr, 0x03, [0x00, 0x02])
            break
        except IOError:
            pass
    time.sleep(0.015)
   
    try:
        block = bus.read_i2c_block_data(addr, 0, 4)
    except IOError:
        pass
   
    humidity = float(block[2] << 8 | block[3]) / 10
    return humidity

def ReadTemperatureHumidity():
    global block
    WakeSensor()
    while True:
        try:
            bus.write_i2c_block_data(addr, 0x03, [0x00, 0x04])
            break
        except IOError:
            pass
    time.sleep(0.015)
   
    try:
        block = bus.read_i2c_block_data(addr, 0, 6)
    except IOError:
        pass
   
    humidity = float(block[2] << 8 | block[3]) / 10
    temperature = float(block[4] << 8 | block[5]) / 10
    return temperature, humidity
