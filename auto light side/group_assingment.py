import time
import _json
from tb_device_mqtt import TBDeviceMqttClient, TBPublishInfo
import serial
import re
import pymysql


MQTTserver = "192.168.136.176" 
DeviceToken = "lyiKHONyFNWd9MEk1AQl"

def uploaddistance():
    while True:
        dervice = '/dev/ttyS0'
        arduino = serial.Serial(dervice,9600)
        output = str(arduino.readline())
        
        current_distance = re.search(r'\d+', output).group()
        
        print(current_distance)
        telemetry_with_ts = {"distance": current_distance}
        client = TBDeviceMqttClient(MQTTserver, DeviceToken)
        client.connect()
        result = client.send_telemetry(telemetry_with_ts)
        client.disconnect()
        print("SENT")
        time.sleep(1800)
    
uploaddistance()
