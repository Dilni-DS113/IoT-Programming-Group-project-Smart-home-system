import serial  
import pymysql

device = '/dev/ttyS0'

while True:
    arduino = serial.Serial(device,9600)
    date = arduino.readline()
    print(data)
    dbConn = pymysql.connect("localhost","jo","","motorstate_db") or die("connection failed")

    print(dbConn)
    with dbConn:
        cursor = dbConn.cursor()
        cursor.execute("INSERT INTO motorLog (state) VALUES(%s)"%(data))
        dbConn.commit
        cursor.close()