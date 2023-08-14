import serial
import pymysql

device = '/dev/ttyS0'

arduino = serial.Serial(device,9600)
while True:
    measurement = arduino.readline()
    print(measurement)
    dbConn = pymysql.connect("localhost","pi","","distance_db") or die("cound not connect to database")
    
#print(dbConn)
    with dbConn:
        cursor = dbConn.cursor()
        cursor.execute("INSERT INTO distancelog (measurement) VALUES (%s)", measurement)
        dbConn.commit()
        cursor.close()
