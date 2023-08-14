import serial  
import pymysql

device = '/dev/ttyS0'
ser = serial.Serial(device,9600)

while True:
    data = ser.readline()
    print(data)
    dbConn = pymysql.connect("localhost","pi","","motorstate_db") or die("connection failed")

    print(dbConn)
    with dbConn:
        cursor = dbConn.cursor()
        cursor.execute("INSERT INTO motorLog(state) VALUES(%s)",data)
        dbConn.commit
        cursor.close()