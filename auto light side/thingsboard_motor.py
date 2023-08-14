import time
import _json
from tb_device_mqtt import TBDeviceMqttClient, TBPublishInfo
import serial
import re
import pymysql

MQTTserver = "192.168.230.176"
DeviceToken = "TuoaOwDU9alsLtal4hSo"

def uploadblinds():
    while True:
        dervice = '/dev/ttyS0'
        arduino = serial.Serial(dervice,9600)
        output = str(arduino.readline())
        current = re.search(r'[a-zA-Z]+', output).group()
        
        print(output)
        telemetry_with_ts = {"Currently": 160}
        client = TBDeviceMqttClient(MQTTserver, DeviceToken)
        client.connect()
        result = client.send_telemetry(telemetry_with_ts)
        client.disconnect()
        print("SENT")
        time.sleep(1800)
    
uploadblinds()
